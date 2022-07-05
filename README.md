# PokerGame
### 포커 게임 프로젝트

텍사스 홀덤 룰을 적용하여 컴퓨터와 포커 게임을 겨루는 프로그램입니다.

<img width="327" alt="mainGame" src="https://user-images.githubusercontent.com/96714275/177181016-4e9d36ae-334c-454d-9d1e-676b59cd7707.PNG">


텍사스 홀덤 룰과 동일하게 자신의 패와 커뮤니티 카드 패를 보고 자신의 판돈을 결정하여 게임을 진행하는 방식입니다.


*****

### 참여자
hcm1206(현창민)

mnyu(조영재)

*****

<img width="523" alt="JokboTest" src="https://user-images.githubusercontent.com/96714275/177181053-1677604f-fe2f-4b36-a754-e3e355e20690.PNG">

<b>현재 테스트 중인 족보 판정 파일</b>

*****

### 진행도(최근 1주)

#### Changelogs 22-07-04
- 일부 족보 판정 오류를 수정했습니다.
- *현재 A 투페어 판정 오류, 플러시 숫자 판정 오류 발생 확인*

#### Changelogs 22-07-04
**MAJOR UPDATE**
- **게임의 승패 판정을 추가하였습니다.**
- 이제 게임 종료 후 각자의 족보를 확인하여 족보가 높은 쪽이 승리하여 판돈을 모두 가져가게 됩니다.
- 게임 종료 후 각 패의 최고 족보가 표시되도록 하였습니다.
- 족보 테스트 파일에서 족보 판정 부분을 별개의 파일(CheckJokbo.py)로 분리하였습니다.
- 로열 스트레이트 판정 버그 등 현재까지 발견된 족보 판정 매커니즘 오류를 수정했습니다.
- *아직 족보 판정 알고리즘 및 메인 게임에 오류가 있을 수 있으므로 발견 즉시 제보해주시기 바랍니다.*

#### Changelogs 22-07-02
- 족보 테스트 파일의 스트레이트 플러시 판정 버그를 비롯한 여러 메커니즘 오류를 수정하였습니다.
- *족보 테스트 파일에서 추가적인 오류 발견 시 바로 제보해주시기 바랍니다.*

#### Changelogs 22-07-01
- **이제 족보 판정용 테스트 파일에서 모든 포커 족보를 판정할 수 있습니다.**
- 두번째 족보 테스트 파일을 추가했습니다. 이 파일은 족보 판정과 동시에 해당 족보에 포함된 숫자 중 가장 높은 숫자를 출력하는 기능이 추가된 파일입니다.
- 두번째 족보 테스트 파일에서 **'점수제' 시스템**을 테스트 중입니다. 이는 양쪽이 똑같은 족보일 때 카드 숫자에 따라 승패를 결정하기 위한 요소입니다.
- *현재 스트레이트 플러시 판정에 버그가 보고되고 있습니다. (추후 해결 예정)*

#### Changelogs 22-06-29
- 게임 룰 변경 : 이제 5번째 커뮤니티 카드 공개 후에도 액션(배팅, 폴드 등)이 가능합니다.
- 배팅과 체크 방식을 변경하였습니다. (이제 체크 시 추가 배팅금은 0원이고 배팅시 최소배팅액을 비활성화하였습니다.)
- 최소배팅액을 비활성화함에 따라 UI에 최소배팅액 대신 현재 블라인드 액수가 표시되도록 하였습니다.
- 이제 참여자 중 하나가 소지한 잔금을 모두 잃으면 게임의 최종 승패가 결정되어 게임이 종료됩니다.
- 모든 참여자의 소지금까지 초기화하는 '게임 초기화' 기능이 추가되었습니다.
- '게임 초기화' 버튼은 게임 상단 메뉴바에서 실행 가능하며 또한 게임의 최종 승패 결정 후 첫번째 버튼으로 활성화됩니다.
- *게임 룰 및 배팅 시스템은 게임 시스템이 구축되며 추가적으로 계속 변경될 예정입니다.*






