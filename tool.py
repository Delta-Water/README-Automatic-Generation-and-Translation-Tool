import os
import json
import requests
from openai import OpenAI
from git import Repo

# Configure translation languages
TRANSLATION_LANGUAGES = ['简体中文', '繁体中文', 'English', 'Español', 'Français', 'Deutsch', '日本語']

LANGUAGE_SWITCH_HEADER = {
    '简体中文': '语言切换',
    '繁体中文': '语言切换',
    'English': 'Language Switch',
    'Español': 'Cambio de idioma',
    'Français': 'Changement de langue',
    'Deutsch': 'Sprachwechsel',
    '日本語': '言語切替'
}

def load_config(config_file='config.json'):
    with open(config_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_repo_files(repo_name, owner, github_token):
    api_url = f'https://api.github.com/repos/{owner}/{repo_name}/contents'
    headers = {'Authorization': f'token {github_token}'}
    
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Unable to retrieve repository files:", response.json())  # 无法检索仓库文件
        return None

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

def summarize_file_content(client, file_name, file_content):
    prompt = (
        f"Please generate a brief summary for the following file:\n"
        f"File Name: {file_name}\n"
        f"File Content:\n{file_content}\n\n"
        f"Please provide a brief description of the main functionality and purpose of the file."
    )
    return call_openai_api(client, prompt)

def generate_readme_content(client, files, github_token, main_language, ignore_patterns):
    file_summaries = []
    for file in files:
        if file['type'] == 'file' and not any(file['name'].startswith(pattern) for pattern in ignore_patterns):
            content = get_file_content(file['download_url'], github_token)
            if content:
                summary = summarize_file_content(client, file['name'], content)
                if summary:
                    file_summaries.append(summary)

    if not file_summaries:
        return None

    all_file_summaries = "\n".join(file_summaries)
    
    prompt = (
        f"Please use {main_language} to generate a professional and engaging README file based on the following file summaries:\n"
        f"File Summaries:\n{all_file_summaries}\n\n"
        f"Please ensure the README includes sections such as project introduction, installation steps, usage instructions, and contribution guidelines, and use Markdown format."
        f"Please add emojis appropriately to make it more engaging."
    )
    
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

def update_readme_with_links(readme_content, translations, main_language):
    readme_with_links = f"## README\n\n"
    readme_with_links += f"### {LANGUAGE_SWITCH_HEADER[main_language]}\n"
    
    for lang in translations.keys():
        readme_with_links += f"- [{lang}](README/README_{lang}.md)\n"

    readme_with_links += "\n" + readme_content  # 添加主语言内容
    return readme_with_links

def commit_changes(repo_name, owner, github_token, updated_readme, translations, branch):
    try:
        # Clone the repository using GitHub Token
        repo = Repo.clone_from(f'https://{github_token}@github.com/{owner}/{repo_name}.git', f'./{repo_name}', branch=branch)
    except Exception as e:
        print(f"Failed to clone the repository: {e}")  # 克隆仓库失败
        return

    # Update the main README file
    readme_path = f'./{repo_name}/README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_readme)
  
    readme_path = f'./{repo_name}/README'
    if not os.path.exists(readme_path):
      os.makedirs(readme_path)
  
    # Update translation files
    for lang, translation in translations.items():
        translation_path = f'{readme_path}/README_{lang}.md'
        with open(translation_path, 'w', encoding='utf-8') as f:
            # Add link to the main README
            f.write("[Back to main language README](README.md)")
            f.write(f"\n\n{translation}")

    repo.git.add('README.md')
    for lang in translations.keys():
        repo.git.add(f'README/README_{lang}.md')
    
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

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=base_url)
    files = get_repo_files(repo_name, owner, github_token)

    if files:
        print("Generating README content...")  # 正在生成 README 内容
        readme_content = generate_readme_content(client, files, github_token, main_language, ignore_patterns)
        if readme_content:
            print("Generating translations...")  # 正在生成翻译
            translations = create_translations(client, readme_content, main_language)
            updated_readme = update_readme_with_links(readme_content, translations, main_language)
            commit_changes(repo_name, owner, github_token, updated_readme, translations, branch)
            print("README file and translation files have been updated and committed to the repository.")  # README 文件和翻译文件已更新并提交到仓库
        else:
            print("Failed to generate README content, operation terminated.")  # 生成 README 内容失败，操作终止
    else:
        print("Failed to retrieve repository files, operation terminated.")  # 无法检索仓库文件，操作终止

if __name__ == "__main__":
    main()