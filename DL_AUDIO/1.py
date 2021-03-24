"""
2021.03.19
토크ON세미나 - 딥러닝 기반 음성인식 기초 1강

"""

"""
Sound ?
소리 = 진동으로 인한 공기의 압축
압축이 얼마나 되었는가 ? = Wave(파동)
파동 : 소리가 진동하며 공간/매질을 전파해 나가는 현상이다. 
      질량의 이동은 없지만 에너지/운동량의 운반은 존재한다.
      
소리에서 얻을 수 있는 물리량
진폭(Amplitude,Intensity), 주파수(Frequency), 위상(Phase, Degress of displacement)

물리 음향 
- Intensity(소리 진폭의 세기), Frequency(소리 떨림의 빠르기), Tone-Color(소리 파동의 모양)
심리 음향 
- Loudness, Pitch, Timbre

Frequency? The number of compressed
단위는 Hertz를 사용, 1Hz는 1초에 한번 진동함을 의미한다.
주기 : 파동이 한번 진동하는 데 걸리는 시간, 또는 그 길이, 일반적으로 sin함수의 주기는 2pie/w
주파수 : 1초 동안의 진동 회수
** 소리의 높낮이는 음원의 주파수에 의해 결정, 주파수가 높으면 고음 낮으면 저음

우리가 사용하는 대부분의 소리들은 복합파이다.
Complex wave는 복수의 서로 다른 정현파들의 합으로 이루어진 파형이다.

input으로 들어오는 오디오파일들은 거의 다 amplitude(진폭)만 기록되는데,
frequency 영역을 얻기위해 푸리에 변환한다.
그 결과는 실수부 + 허수부이고
이 복소수의 절대값은 Spectrum magnitude라 부르며 주파수의 강도를 뜻한다.
복소수가 가지는 phase는 phase sectrum(주파수의 위상)이라고 부른다.

Audio Task
 - Sound 
    Speech Classification & Auto-tagging(Acoustic Scene / Event Indentification)
 - Speech
    Speech Recognition(STT), Speech Synthesis(TTS), Speech Style Transfer(STS)

















"""