import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Problem, ProblemClass



rank_list = ['', 'B5', 'B4', 'B3', 'B2', 'B1', 'S5', 'S4', 'S3', 'S2', 'S1',  
            'G5', 'G4', 'G3', 'G2', 'G1', 'P5', 'P4', 'P3', 'P2', 'P1',
            'D5', 'D4', 'D3', 'D2', 'D1', 'R5', 'R4', 'R3', 'R2', 'R1']


rank_dic = {
    'Sprout' : 'B5','Unrated' : 'UR',
    'Bronze V' : 'B5','Bronze IV' : 'B4','Bronze III' : 'B3','Bronze II' : 'B2','Bronze I' : 'B1',
    'Silver V' : 'S5','Silver IV' : 'S4','Silver III' : 'S3','Silver II' : 'S2','Silver I' : 'S1',
    'Gold V' : 'G5','Gold IV' : 'G4','Gold III' : 'G3','Gold II' : 'G2','Gold I' : 'G1',
    'Platinum V' : 'P5','Platinum IV' : 'P4','Platinum III' : 'P3','Platinum II' : 'P2','Platinum I' : 'P1',
    'Diamond V' : 'D5','Diamond IV' : 'D4','Diamond III' : 'D3','Diamond II' : 'D2','Diamond I' : 'D1',
    'Ruby V' : 'R5','Ruby IV' : 'R4','Ruby III' : 'R3','Ruby II' : 'R2','Ruby I' : 'R1',
}


# 유저가 푼 문제를 보여주는 사이트를 랜더하는 함수
def solved(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    solved_problems = person.solved_problems.all()
    rank_dic = {'B' : 0,'S' : 0,'G' : 0,'P' : 0,'D' : 0,'R' : 0,'UR' : 0,}
    class_dic = {
    }
    # django aggregate and django join 공부하기
    for solved_problem in solved_problems:
        if solved_problem.rank[0] == 'B':
            rank_dic['B'] += 1
        elif solved_problem.rank[0] == 'S':
            rank_dic['S'] += 1
        elif solved_problem.rank[0] == 'G':
            rank_dic['G'] += 1
        elif solved_problem.rank[0] == 'P':
            rank_dic['P'] += 1
        elif solved_problem.rank[0] == 'D':
            rank_dic['D'] += 1
        elif solved_problem.rank[0] == 'R':
            rank_dic['R'] += 1
        elif solved_problem.rank[0] == 'U':
            rank_dic['UR'] += 1

        for classs in solved_problem.classes.all():
            class_dic[classs.name] = class_dic.setdefault(classs.name, 0) + 1

    # # 그래프 그리기
    # x = list(rank_dic.keys())
    # y = list(rank_dic.values())
    # x.reverse()
    # y.reverse()

    # plt.clf()

    # plt.barh(x, y)
    # plt.title(f"{request.user.username}가 푼 문제")
    # plt.ylabel('푼 문제 수')
    # plt.xlabel('문제 티어')
    
    # # 비어있는 버퍼를 생성
    # buffer = BytesIO()

    
    # # 버퍼에 그래프를 저장
    # plt.savefig(buffer, format='png')

    # # 버퍼의 내용을 base64 로 인코딩
    # image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    # # 버퍼를 닫아줌
    # buffer.close()
    context = {
        'person' : person,
        'rank_dic' : rank_dic,
        'class_dic' : class_dic,
        # 'chart_image': f'data:image/png;base64,{image_base64}',
    }


    return render(request,'algorithms/test.html', context)


# 닉네임에 해당하는 유저 프로필에서 푼 문제들과 랭크를 가져오는 크롤링
def solved_crawling(request, user_pk):
    person = get_user_model().objects.get(pk=user_pk)
    nickname = person.beakjoon_nickname
    url = f'https://www.acmicpc.net/user/{nickname}'
    
    # 크롤링으로 html 파일 전체 가져오기
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = response.text

    # html파일에서 필요한 부분 파싱하기
    soup = BeautifulSoup(html, "html.parser")
    solved_list = soup.select(".problem-list a")
    beakjoon_rank_tag = soup.select_one(".solvedac-tier")
    beakjoon_rank = rank_list[int(beakjoon_rank_tag.get("src").split('tier/')[-1].strip('.svg'))]
    solved_num_list = [link.get("href").lstrip('/problem/') for link in solved_list ]

    # 이를 활용하여 user DB에 데이터 추가
    person.beakjoon_rank = beakjoon_rank
    person.save()

    for solved_num in solved_num_list:
        problem = Problem.objects.get(problem_num=solved_num) 
        problem.solved_users.add(person)

    return redirect('algorithms:solved', person.pk)


