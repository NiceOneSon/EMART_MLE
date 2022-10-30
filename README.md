# EMART_MLE

# EMART ML Engineer

금번 채용 과정 중 과제 전형에 따른 테스트 결과서 입니다.

### 테스트 결과서

1. Docker Build
   
   <img width="380" alt="Untitled" src="https://user-images.githubusercontent.com/103669413/198397983-a343eff5-2a6d-41ef-80d3-f35de70a89ea.png">
    
2. Docker Run
    
    <img width="425" alt="Untitled (1)" src="https://user-images.githubusercontent.com/103669413/198398096-7a4a4402-9627-4fa6-8954-c1d0093bb17b.png">
    
3. REST API Testing

port num 8000으로 테스트 결과 하기 내용과 같습니다.
결과는 Json 형태로 PM10, PM25 두 개의 데이터를 받습니다.
    
   <img width="1635" alt="Untitled (2)" src="https://user-images.githubusercontent.com/103669413/198398241-17d63a30-a1d6-4858-9609-348a8a3d7296.png">

    
4. Test 결과
    1. Test Sample data (20%) RMSE : 4.25
    2. 월 별 데이터 비교
    1월부터 4월까지 각 도표와, 차트입니다.
        - 1월
            
            
            | date | pred_PM10 | real_PM10 | pred_PM25 | real_PM25 |
            | --- | --- | --- | --- | --- |
            | 2021-01-07 | 41.553024 | 38 | 13.060808 | 12 |
            | 2021-01-08 | 24.080496 | 23 | 11.259658 | 11 |
            | 2021-01-09 | 30.347563 | 27 | 17.17633 | 16 |
            | 2021-01-10 | 37.25146 | 41 | 23.066729 | 28 |
            | 2021-01-11 | 50.005524 | 53 | 33.62785 | 37 |
            | 2021-01-12 | 64.90857 | 69 | 48.091255 | 53 |
            | 2021-01-13 | 110.00624 | 111 | 51.30989 | 50 |
            | 2021-01-14 | 82.38222 | 88 | 29.801573 | 26 |
            | 2021-01-15 | 81.97414 | 87 | 34.060028 | 32 |
            | 2021-01-16 | 58.849754 | 60 | 38.32709 | 38 |
            | 2021-01-17 | 21.63469 | 22 | 12.47684 | 14 |
            | 2021-01-18 | 34.592377 | 39 | 17.63292 | 18 |
            | 2021-01-19 | 28.52966 | 33 | 15.386126 | 14 |
            | 2021-01-20 | 47.76318 | 51 | 26.365005 | 28 |
            | 2021-01-21 | 48.948277 | 53 | 29.969093 | 31 |
            | 2021-01-22 | 42.055725 | 46 | 30.801994 | 31 |
            | 2021-01-23 | 10.346312 | 14 | 7.534932 | 9 |
            | 2021-01-24 | 11.533145 | 12 | 7.775069 | 8 |
            | 2021-01-25 | 21.526623 | 24 | 13.861759 | 15 |
            | 2021-01-26 | 43.785286 | 48 | 27.289371 | 30 |
            | 2021-01-27 | 39.623665 | 43 | 18.119736 | 19 |
            | 2021-01-28 | 33.079014 | 35 | 15.261412 | 15 |
            | 2021-01-29 | 22.387371 | 24 | 9.640155 | 10 |
            | 2021-01-30 | 52.834732 | 55 | 23.32058 | 24 |
            | 2021-01-31 | 49.65144 | 62 | 26.58119 | 29 |
            
            ![Untitled (3)](https://user-images.githubusercontent.com/103669413/198398436-cfd13170-366b-4f2f-91bf-cab7ca0f3ab2.png)
            
        - 2월
            
            
            | date | pred_PM10 | real_PM10 | pred_PM25 | real_PM25 |
            | --- | --- | --- | --- | --- |
            | 2021-02-01 | 66.93231 | 76 | 38.48226 | 37 |
            | 2021-02-02 | 28.232407 | 34 | 16.342743 | 17 |
            | 2021-02-03 | 30.440657 | 38 | 18.289244 | 20 |
            | 2021-02-04 | 22.644634 | 27 | 13.643778 | 16 |
            | 2021-02-05 | 25.71584 | 32 | 15.610465 | 17 |
            | 2021-02-06 | 64.76311 | 67 | 39.111305 | 37 |
            | 2021-02-07 | 86.88496 | 93 | 55.10908 | 50 |
            | 2021-02-08 | 25.77026 | 29 | 15.282055 | 16 |
            | 2021-02-09 | 24.07048 | 25 | 14.370734 | 14 |
            | 2021-02-10 | 35.090694 | 38 | 22.292688 | 22 |
            | 2021-02-11 | 70.40311 | 77 | 49.420143 | 49 |
            | 2021-02-12 | 88.468475 | 92 | 63.341785 | 60 |
            | 2021-02-13 | 91.496376 | 94 | 65.459625 | 64 |
            | 2021-02-14 | 83.11885 | 99 | 62.278675 | 66 |
            | 2021-02-15 | 52.672592 | 63 | 36.646324 | 41 |
            | 2021-02-16 | 21.016617 | 25 | 12.069715 | 12 |
            | 2021-02-17 | 39.835297 | 44 | 12.54443 | 9 |
            | 2021-02-18 | 44.06014 | 46 | 15.148677 | 14 |
            | 2021-02-19 | 48.130825 | 51 | 24.557552 | 25 |
            | 2021-02-20 | 65.133095 | 75 | 37.63278 | 34 |
            | 2021-02-21 | 84.72437 | 85 | 47.837536 | 46 |
            | 2021-02-22 | 55.28634 | 60 | 27.712666 | 25 |
            | 2021-02-23 | 53.020885 | 57 | 15.324924 | 14 |
            | 2021-02-24 | 52.86441 | 56 | 20.829866 | 22 |
            | 2021-02-25 | 54.592964 | 62 | 29.65506 | 31 |
            | 2021-02-26 | 38.012054 | 44 | 22.017525 | 23 |
            | 2021-02-27 | 15.490236 | 21 | 9.446382 | 11 |
            | 2021-02-28 | 21.170582 | 26 | 12.473009 | 14 |
            
            ![Untitled (4)](https://user-images.githubusercontent.com/103669413/198398494-49242581-007a-4c75-a090-59523ba2091e.png)
            
        - 3월
            
            
            | date | pred_PM10 | real_PM10 | pred_PM25 | real_PM25 |
            | --- | --- | --- | --- | --- |
            | 2021-03-01 | 15.92334 | 18 | 9.895663 | 10 |
            | 2021-03-02 | 8.942026 | 10 | 4.398529 | 5 |
            | 2021-03-03 | 35.7669 | 45 | 21.679943 | 23 |
            | 2021-03-04 | 41.18712 | 55 | 25.847942 | 30 |
            | 2021-03-05 | 41.06337 | 45 | 23.66113 | 23 |
            | 2021-03-06 | 31.730783 | 36 | 18.910458 | 18 |
            | 2021-03-07 | 22.802055 | 25 | 13.340811 | 12 |
            | 2021-03-08 | 39.409817 | 47 | 24.00756 | 24 |
            | 2021-03-09 | 44.54326 | 50 | 27.21467 | 27 |
            | 2021-03-10 | 89.730736 | 105 | 61.332027 | 63 |
            | 2021-03-11 | 121.335266 | 130 | 86.39636 | 80 |
            | 2021-03-12 | 69.52275 | 76 | 44.419434 | 43 |
            | 2021-03-13 | 53.521477 | 61 | 33.42785 | 33 |
            | 2021-03-14 | 89.04875 | 93 | 57.74877 | 57 |
            | 2021-03-15 | 77.98031 | 100 | 55.519665 | 58 |
            | 2021-03-16 | 77.43481 | 102 | 17.973385 | 12 |
            | 2021-03-17 | 100.807945 | 113 | 19.31601 | 13 |
            | 2021-03-18 | 103.95292 | 112 | 45.057755 | 39 |
            | 2021-03-19 | 77.39359 | 81 | 24.739212 | 25 |
            | 2021-03-20 | 25.451756 | 39 | 12.761743 | 10 |
            | 2021-03-21 | 35.06035 | 0 | 20.44315 | 0 |
            | 2021-03-22 | 22.313477 | 43 | 9.373937 | 16 |
            | 2021-03-23 | 61.742443 | 85 | 21.59179 | 28 |
            | 2021-03-24 | 55.496258 | 90 | 30.64544 | 36 |
            | 2021-03-25 | 53.84346 | 72 | 29.07831 | 37 |
            | 2021-03-26 | 90.80694 | 124 | 47.02877 | 84 |
            | 2021-03-27 | 67.31174 | 76 | 38.95594 | 43 |
            | 2021-03-28 | 16.686497 | 20 | 10.867267 | 14 |
            | 2021-03-29 | 257.09564 | 312 | 46.325375 | 57 |
            | 2021-03-30 | 122.70744 | 175 | 25.439257 | 34 |
            
            ![Untitled (5)](https://user-images.githubusercontent.com/103669413/198398543-80c440a0-6e8f-419b-8c87-75308dbaeabd.png)
            
        - 4월
            
            
            | date | pred_PM10 | real_PM10 | pred_PM25 | real_PM25 |
            | --- | --- | --- | --- | --- |
            | 2021-04-01 | 40.134018 | 48 | 13.620445 | 16 |
            | 2021-04-02 | 48.478092 | 53 | 13.91754 | 14 |
            | 2021-04-03 | 35.99491 | 40 | 13.724499 | 16 |
            | 2021-04-04 | 12.251518 | 10 | 5.491359 | 5 |
            | 2021-04-05 | 20.18902 | 23 | 10.57851 | 11 |
            | 2021-04-06 | 37.08303 | 43 | 20.91623 | 23 |
            | 2021-04-07 | 52.40708 | 63 | 31.716501 | 39 |
            | 2021-04-08 | 34.63095 | 36 | 15.8067 | 16 |
            | 2021-04-09 | 31.175346 | 37 | 16.044662 | 18 |
            | 2021-04-10 | 31.801027 | 37 | 17.549591 | 20 |
            | 2021-04-11 | 45.139317 | 49 | 24.65938 | 26 |
            | 2021-04-12 | 38.014618 | 44 | 21.730265 | 24 |
            | 2021-04-13 | 13.355633 | 15 | 8.235024 | 8 |
            | 2021-04-14 | 24.118187 | 29 | 12.156639 | 15 |
            | 2021-04-15 | 50.23864 | 52 | 24.906883 | 26 |
            | 2021-04-16 | 76.91289 | 81 | 17.627728 | 18 |
            | 2021-04-17 | 84.35558 | 89 | 16.401978 | 16 |
            | 2021-04-18 | 31.19479 | 33 | 13.143918 | 13 |
            | 2021-04-19 | 40.884216 | 51 | 18.922676 | 23 |
            | 2021-04-20 | 67.21653 | 75 | 34.086887 | 37 |
            | 2021-04-21 | 69.134186 | 81 | 36.891113 | 38 |
            | 2021-04-22 | 69.47028 | 80 | 36.718597 | 40 |
            | 2021-04-23 | 41.917053 | 48 | 22.305067 | 24 |
            | 2021-04-24 | 23.47054 | 24 | 11.439592 | 11 |
            | 2021-04-25 | 25.451202 | 27 | 11.336968 | 13 |
            | 2021-04-26 | 27.523903 | 30 | 12.416232 | 14 |
            | 2021-04-27 | 30.306559 | 33 | 14.193496 | 16 |
            | 2021-04-28 | 65.84343 | 69 | 24.171314 | 26 |
            | 2021-04-29 | 58.769573 | 73 | 19.3532 | 22 |
            | 2021-04-30 | 33.97409 | 38 | 16.46458 | 17 |
            
            ![Untitled (6)](https://user-images.githubusercontent.com/103669413/198398574-034d958a-2bc0-4d91-b339-0b1c532d4516.png)

5. 아키텍처 제안
    
    부하 분산 및 급격한 트래픽 변화에 대응하기 위해서는 GCP 내 GKE에서 제공하는 Auto Scaling을 사용할 거 같습니다.
    아무래도 평상시와 다르게 특정 시간대 트래픽이 몰려서 노드가 더 필요해진다면 유동적으로 노드(서버)를 관리해야합니다.
    GKE 또는 K8s는 이러한 인프라 관리를 위해 두 가지 Auto Scaling 기능을 갖추고 있습니다.
    
    1. HPA(Horizontal Pods Autoscler)
    2. CA(Cluster Autoscaler)
    
    → HPA는 실행되는 Pods(Container)가 기준치 이상의 자원을 사용하게 된다면 Container를 더 늘려 로드 밸런싱을 사용하게 됩니다. Master 노드에서는 Container를 실행할 Slave Node에 빌드하게 됩니다.
    → CA는 새로운 Container를 실행하고 싶은데 적절한 노드가 없을 경우 노드를 추가로 늘리는 것을 의미합니다.