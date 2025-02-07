import os
import json
import requests
from openai import OpenAI
from git import Repo

# 配置翻译语言
TRANSLATION_LANGUAGES = ['简中', '繁中', 'Español', 'Français', 'Deutsch', '日本語']

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
        print("无法获取仓库文件:", response.json())
        return None

def get_file_content(file_url, github_token):
    headers = {'Authorization': f'token {github_token}'}
    response = requests.get(file_url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        print("无法获取文件内容:", response.json())
        return None

def call_openai_api(client, prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"API调用失败: {e}")
        return None

def summarize_file_content(client, file_name, file_content):
    prompt = (
        f"请为以下文件生成一个简要的总结：\n"
        f"文件名：{file_name}\n"
        f"文件内容：\n{file_content}\n\n"
        f"请提供文件的主要功能和用途的简要描述。"
    )
    return call_openai_api(client, prompt)

def generate_readme_content(client, files, github_token):
    file_summaries = []
    for file in files:
        if file['type'] == 'file':
            content = get_file_content(file['download_url'], github_token)
            if content:
                summary = summarize_file_content(client, file['name'], content)
                if summary:
                    file_summaries.append(summary)

    if not file_summaries:
        return None

    all_file_summaries = "\n".join(file_summaries)
    
    prompt = (
        f"请根据以下文件总结生成一个专业且吸引人的README文件：\n"
        f"文件总结：\n{all_file_summaries}\n\n"
        f"请确保README包含项目简介、安装步骤、使用说明和贡献指南等部分，并使用Markdown格式。"
    )
    
    return call_openai_api(client, prompt)

def translate_text(client, text, target_language):
    prompt = f"请将以下文本翻译成{target_language}，并适当添加emoji，使其更具吸引力：\n{text}"
    return call_openai_api(client, prompt)

def create_translations(client, readme_content, main_language):
    translations = {}
    
    for lang in TRANSLATION_LANGUAGES:
        if lang == main_language:
            continue
        print(f"正在翻译为 {lang}...")
        translation = translate_text(client, readme_content, lang)
        if translation:
            translations[lang] = translation
        else:
            print(f"翻译 {lang} 失败，跳过该语言。")
    
    return translations

def update_readme_with_links(readme_content, translations, main_language):
    readme_with_links = f"## README\n\n### 语言切换:\n"
    readme_with_links += f"- [主语言: {main_language}](README.md)\n"
    
    for lang in translations.keys():
        readme_with_links += f"- [{lang}](README_{lang}.md)\n"

    readme_with_links += "\n" + readme_content  # 添加主语言的内容
    return readme_with_links

def commit_changes(repo_name, owner, github_token, updated_readme, translations, branch):
    try:
        # 使用 GitHub Token 进行克隆
        repo = Repo.clone_from(f'https://{github_token}@github.com/{owner}/{repo_name}.git', f'./{repo_name}', branch=branch)
    except Exception as e:
        print(f"克隆仓库失败: {e}")
        return

    # 更新主README文件
    readme_path = f'./{repo_name}/README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_readme)

    # 更新翻译文件
    for lang, translation in translations.items():
        translation_path = f'./{repo_name}/README_{lang}.md'
        with open(translation_path, 'w', encoding='utf-8') as f:
            f.write(translation)

    repo.git.add('README.md')
    for lang in translations.keys():
        repo.git.add(f'README_{lang}.md')
    
    repo.index.commit('自动生成README文件，添加翻译文件')
    
    try:
        # 使用 GitHub Token 进行推送
        repo.git.push(f'https://{github_token}@github.com/{owner}/{repo_name}.git', branch)
    except Exception as e:
        print(f"推送更改失败: {e}")

def main():
    config = load_config()
    
    repo_name = config['repo_name']
    owner = config["owner"]
    github_token = os.getenv('GITHUB_TOKEN')
    base_url = config['base_url']
    branch = config.get('branch', 'main')
    main_language_index = config['main_language_index']
    main_language = TRANSLATION_LANGUAGES[main_language_index]

    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url=base_url)
    files = get_repo_files(repo_name, owner, github_token)

    if files:
        print("正在生成README内容...")
        readme_content = generate_readme_content(client, files, github_token)
        if readme_content:
            print("正在生成翻译...")
            translations = create_translations(client, readme_content, main_language)
            updated_readme = update_readme_with_links(readme_content, translations, main_language)
            commit_changes(repo_name, owner, github_token, updated_readme, translations, branch)
            print("README文件及翻译文件已更新并提交到仓库。")
        else:
            print("未能生成README内容，操作终止。")
    else:
        print("未能获取仓库文件，操作终止。")

if __name__ == "__main__":
    main()