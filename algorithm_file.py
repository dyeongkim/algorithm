import os
import requests
from bs4 import BeautifulSoup

def get_existing_folders(base_path):
    existing_folders = []
    for item in os.listdir(base_path):
        folder_path = os.path.join(base_path, item)
        if os.path.isdir(folder_path):
            existing_folders.append(item)
    return existing_folders

def create_problem_file(problem_number, site, problem_type):
    url = f"https://www.acmicpc.net/problem/{problem_number}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    # 문제 사이트
    if site == 1:
        base_path = "BOJ_baekjoon"
    elif site == 2:
        base_path = "codeup"
    else:
        print("잘못된 문제 사이트입니다.")
        return

    # 문제유형 선택
    existing_folders = get_existing_folders(base_path)
    if existing_folders:
        print("기존 폴더 목록:")
        for i, folder in enumerate(existing_folders, start=1):
            print(f"{i}. {folder}")
        problem_type = int(input("문제 유형 폴더를 선택하세요 (번호 입력): "))
        problem_type_path = os.path.join(base_path, existing_folders[problem_type - 1])
    else:
        problem_type_path = os.path.join(base_path, str(problem_type))
        os.makedirs(problem_type_path)
    
    # 크롤링
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        problem_title = soup.select_one("#problem_title").text.strip()
        problem_description = soup.select_one("#problem_description").get_text(separator="\n", strip=True)
        problem_input = soup.select_one("#problem_input").get_text(separator="\n", strip=True)
        problem_output = soup.select_one("#problem_output").get_text(separator="\n", strip=True)

        # 파일생성
        filename = os.path.join(problem_type_path, f"boj_{problem_number}.py")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"# 백준 {problem_number} - {problem_title}\n\n")
            file.write(f"'''\n")
            file.write(f"# 문제\n{problem_description}\n\n")
            file.write(f"# 입력\n{problem_input}\n\n")
            file.write(f"# 출력\n{problem_output}\n")
            file.write(f"'''\n\n")

        print(f"{filename} 파일이 생성되었습니다.")
    else : 
        print(response.status_code)

if __name__ == "__main__":
    problem_number = input("문제 번호를 입력하세요: ")
    site = int(input("문제 사이트를 입력하세요 (1. 백준, 2. codeup): "))
    create_problem_file(problem_number, site, None)