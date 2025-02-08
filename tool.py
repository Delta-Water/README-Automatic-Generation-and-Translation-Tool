import os
import json
import requests
from openai import OpenAI
from git import Repo

# Configure translation languages
TRANSLATION_LANGUAGES = ['简体中文', '繁体中文', 'English', 'Español', 'Français', 'Deutsch', '日本語']

LANGUAGE_SWITCH_HEADER = {
    '简体中文': '切换语言: 简体中文',
    '繁体中文': '切換語言: 繁體中文',
    'English': 'Switch Language: English',
    'Español': 'Cambiar idioma: Español',
    'Français': 'Changer de langue: Français',
    'Deutsch': 'Sprache wechseln: Deutsch',
    '日本語': '言語を切り替える: 日本語'
}

def load_config(config_file='config.json'):
    with open(config_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_repo_files(repo_name, owner, github_token, path=''):
    api_url = f'https://api.github.com/repos/{owner}/{repo_name}/contents/{path}'
    headers = {'Authorization': f'token {github_token}'}
    
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        items = response.json()
        all_files = []
        file_structure = {}
        
        for item in items:
            if item['type'] == 'dir':
                # 递归获取目录内容
                sub_files, sub_structure = get_repo_files(repo_name, owner, github_token, item['path'])
                all_files.extend(sub_files)
                file_structure[item['path']] = sub_structure  # 将子目录结构添加到文件结构中
            else:
                all_files.append(item)
                file_structure[item['path']] = item['name']  # 将文件添加到文件结构中
        
        return all_files, file_structure  # 返回文件列表和文件结构
    else:
        print("Unable to retrieve repository files:", response.json())  # 无法检索仓库文件
        return None, None  # 返回 None

def get_file_content(file_url, github_token):
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(file_url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        print("Unable to retrieve file content:", response.json())  # 无法检索文件内容
        return None

def call_openai_api(client, prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"API call failed: {e}")  # API 调用失败
        return None

def summarize_file_content(client, file_path, file_content):
    prompt = (
        f"Please generate a brief summary for the following file:\n"
        f"File path: {file_path}\n"
        f"File Content:\n{file_content}\n\n"
        f"Please provide a brief description of the main functionality and purpose of the file."
    )
    print(f"Summing up: {file_path}")
    return call_openai_api(client, prompt)

def generate_readme_content(client, files, github_token, main_language, ignore_patterns, ignore_paths, file_structure):
    file_summaries = []
    for file in files:
        if any(path in file['path'] for path in ignore_paths):
            continue

        if file['type'] == 'file' and not any(file['name'].startswith(pattern) for pattern in ignore_patterns):
            content = get_file_content(file['download_url'], github_token)
            if content:
                summary = summarize_file_content(client, file['path'], content)
                if summary:
                    file_summaries.append(summary)

    if not file_summaries:
        return None

    all_file_summaries = "\n".join(file_summaries)

    # 将文件结构信息添加到 README 内容生成的提示中
    structure_info = json.dumps(file_structure, ensure_ascii=False, indent=2)  # 格式化文件结构为 JSON 字符串
    prompt = (
        f"Please use {main_language} to generate a professional and engaging README file based on the following project structure and file summaries:\n"
        f"Project Structure:\n{structure_info}\n\n"
        f"File Summaries:\n{all_file_summaries}\n\n"
        f"Use emoticons and witty language to make this descriptive document more interesting."
        f"This is a direct output to the production environment, so please do not provide anything to be modified"
    )
    print(f"Generating README file.")
    return call_openai_api(client, prompt)

def translate_text(client, text, target_language):
    prompt = f"Please translate the following text into {target_language}, and reserve emojis to make it more engaging:\n{text}"
    return call_openai_api(client, prompt)

def create_translations(client, readme_content, main_language):
    translations = {}
    
    for lang in TRANSLATION_LANGUAGES:
        if lang == main_language:
            continue
        print(f"Translating to {lang}...")  # 正在翻译到 {lang}...
        translation = translate_text(client, readme_content, lang)
        if translation:
            translations[lang] = translation
        else:
            print(f"Translation to {lang} failed, skipping this language.")  # 翻译到 {lang} 失败，跳过该语言

    return translations

def create_links(language, path, main_language=False):
    if main_language:
        head = "- [{main_language}](README.md)
    else:
        head = ""
    return head + "\n".join(f"- [{value}]({"{readme_path}/README_{lang}.md".format(readme_path=path, lang=key)})" for key, value in LANGUAGE_SWITCH_HEADER.items() if key != language and key != main_language)
        

def update_readme_with_links(readme_content, translations, main_language, path):
    readme_with_links = f"{create_links(main_language, path)}\n\n{readme_content}"
    translations_with_links = {}
    for (language, translation) in translations.items():
        translations_with_links[language] = f"{create_links(language, path, main_language)}\n\n{translation}"

    return readme_with_links, translations_with_links

def commit_changes(repo_name, owner, github_token, updated_readme, translations, branch, readme_path):
    try:
        # Clone the repository using GitHub Token
        repo = Repo.clone_from(f'https://{github_token}@github.com/{owner}/{repo_name}.git', f'./{repo_name}', branch=branch)
    except Exception as e:
        print(f"Failed to clone the repository: {e}")  # 克隆仓库失败
        return

    # Update the main README file
    raw_readme_path = f'./{repo_name}/README.md'
    with open(raw_readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_readme)
  
    os.makedirs(readme_path, exist_ok=True)

    # Update translation files
    for lang, translation in translations.items():
        translation_path = f'./{repo_name}/{readme_path}/README_{lang}.md'
        with open(translation_path, 'w', encoding='utf-8') as f:
            f.write(translation)

    repo.git.add('README.md')
    for lang in translations.keys():
        repo.git.add(f'{readme_path}/README_{lang}.md')
    
    repo.index.commit('Automatically generated README file, added translation files')  # 自动生成的 README 文件，添加翻译文件
    
    try:
        # Push changes using GitHub Token
        repo.git.push(f'https://{github_token}@github.com/{owner}/{repo_name}.git', branch)
    except Exception as e:
        print(f"Failed to push changes: {e}")  # 推送更改失败

def main():
    config = load_config()
    
    repo_name = config['repo_name']
    owner = config["owner"]
    github_token = os.getenv('GITHUB_TOKEN')
    base_url = config['base_url']
    branch = config.get('branch', 'main')
    main_language_index = config['main_language_index']
    main_language = TRANSLATION_LANGUAGES[main_language_index]
    ignore_patterns = config.get('ignore_patterns', [])
    ignore_paths = config.get('ignore_paths', [])
    readme_path = config.get('readme_path', "README")

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=base_url)
    files, file_structure = get_repo_files(repo_name, owner, github_token)

    if files:
        print("Generating README content...")  # 正在生成 README 内容
        readme_content = generate_readme_content(client, files, github_token, main_language, ignore_patterns, ignore_paths, file_structure)
        if readme_content:
            print("Generating translations...")  # 正在生成翻译
            translations = create_translations(client, readme_content, main_language)
            updated_readme, updated_translations = update_readme_with_links(readme_content, translations, main_language, readme_path)
            commit_changes(repo_name, owner, github_token, updated_readme, updated_translations, branch, readme_path)
            print("README file and translation files have been updated and committed to the repository.")  # README 文件和翻译文件已更新并提交到仓库
        else:
            print("Failed to generate README content, operation terminated.")  # 生成 README 内容失败，操作终止
    else:
        print("Failed to retrieve repository files, operation terminated.")  # 无法检索仓库文件，操作终止

if __name__ == "__main__":
    main()