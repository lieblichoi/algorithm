import math

def replace_step(m):
    return m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

def solution(m, musicinfos):
    answer = None
    max_play_time = 0
    m = replace_step(m)
   
    for musicinfo in musicinfos:
        start_time, end_time, name, melody = musicinfo.split(",")
        play_time = int(end_time[:2]) * 60 + int(end_time[3:]) - int(start_time[:2]) * 60 - int(start_time[3:])
       
        melody = replace_step(melody)
       
        # ABC(3) 라는 melody 가 16초 진행
        # 5번 + 1 -> 6번 반복
        # 올림(실행시간 / 멜로디 길이)
        # ABCABCABCABCABCABC
        # ..............16
       
        melody_repeated_count = math.ceil(play_time/ len(melody))
        melody_played = (melody * melody_repeated_count)[:play_time]
       
        if m in melody_played and play_time > max_play_time:
            answer = name
            max_play_time = play_time
# 자신이 들은 멜로디가 포함되어 있는 음악 중 재생 시간이 제일 긴 음악 제목
    if answer is None:
        return "(None)"
       
    return answer