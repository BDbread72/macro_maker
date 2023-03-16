*Macro!에 오신걸 환영합니다!*
Macro!는 여러가지 게임이나 작업에서 반복적인 작업을 조건문에 맞춰서 하기위해 제작된 프로그램 입니다.
**projects**파일에 프로젝트를 생성하여 새로운 매크로 작업을 제작할 수 있습니다.


***명령어 리스트***
명령어는 아래와같이 작성할 수 있습니다.
```
"commands":{
    "on_start":[
        "명령구문1",
        "명령구문2"

    ]
}
```

*click*<br>
마우스를 클릭합니다.

*mouse_to_img [image]*<br>
[image]의 이미지를 화면에서 감지하여, 해당 위치로 이동합니다. [image]에는 imgs에서 작성하여 저장해야 합니다.<br><br>

*wait [time]*<br>
[time]만큼 기다립니다. 여러가지 오류나, 애니메이션 효과가 나올것을 대비하여 사용하기도 합니다.<br><br>

*move_to [x] [y]*<br>
[x],[y]의 좌표로 마우스를 이동시킵니다.<br><br>

*random_move [randoms] [x1 y1] [x2 y2]*<br>
랜덤한 좌표로 이동합니다. 좌표는 x1,y1 또는, x2,y2처럼 작용합니다. 좌표의 개수는 randoms의 개수와 같아야 합니다.<br>
ex<br>
> random_move 3 100 100 200 200 300 300<br><br>

*run [command_name]*<br>
[command_name]이름을 가진 명령집합을 실행합니다.<br><br>

*anchor [name]*<br>
[name]의 앵커를 만듭니다. return 명령어에 사용됩니다.<br><br>

*return [anchor_name]*<br>
[anchor_name]의 앵커부터 새로 명령어를 실행합니다.<br><br>

*rand_area [x1] [x2] [y1] [y2]*<br>
마우스를 x1부터 x2, y1부터 y2의 범위중 한곳으로 보냅니다.<br><br>

*console [text]*<br>
[text]의 내용을 콘솔로 내보냅니다. 어떤 명령어를 실행했었는지 확인하기 용이합니다.<br><br>

*till img [image] [command]*<br>
화면에서 [image]이미지를 감지할때까지 기다립니다. 감지하면, [command]를 실행합니다. (pass 명령어로 넘길 수 있습니다.)<br><br>

*img_ifs [num_imgs] [img1] [command1] [img2] [command2] ...*<br>
[num_imgs] 개의 이미지를 화면에서 지속적으로 검색합니다. 만약 [img1]이 검색되면, [command1]이 실행됩니다.<br><br>

*limbus_stage_rand 'x y' [up/down] [untill_img]*<br>
[Limbus-Company]<br>
림버스 컴퍼니 거울던전을 위한 스테이지 랜덤 선택 명령어 입니다. 스테이지 이미지를 여러개 입력하면 사용할 수 있습니다.<br><br>

**VAR ...**<br>
var은 매크로 실행중에 사용되는 변수입니다. JSON파일의 vars로 저장됩니다.<br><br>

*var set [name] [value]*<br>
변수 [name]의 값을 [value]으로 정합니다.<br><br>

*var if [name] [comparance] [value] [True_command] [False_command]*<br>
변수 [name]의 값을 [value]와 비교합니다. 결과에 따라 다른 명령어를 실행합니다.<br><br>

*var compare [name1] [comparace] [name2] [True_command] [False_command]*<br>
변수 [name1]의 값과 [name2]의 값을 비교합니다. 결과에 따라 다른 명령어를 실행합니다.<br><br>

*var cal [name] [calculation] [number]*<br>
[name] 변수를 [calculation]에 따라 [number]를 적용합니다. (미 제작)<br><br>

림버스 컴퍼니 전용/관련 명령어 입니다.<br><br>

```
== : 같음<br>
!= : 다름<br>
> : 큼<br>
< : 작음<br>
>= : 크거나 같음<br>
<= : 작거나 같음<br>
```
```
[calculation_value]: 계산식_정리입니다.<br>
+ : 더하기<br>
- : 빼기<br>
* : 곱하기<br>
/ : 나누기<br>
```
