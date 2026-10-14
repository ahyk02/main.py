import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MBTI로 포켓몬 찾기!",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Single-file Streamlit app. The quiz, styles, data, and interactions are embedded below.
HTML = r"""
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MBTI로 포켓몬 찾기!</title>
<style>
:root{--sky:#dff4ff;--sky2:#bde7fb;--pink:#ffe1eb;--pink2:#ffc7dc;--ink:#35445b;--muted:#6b7890;--white:#fffdfd;--blue:#70c4e8;--hot:#f28eb4;--shadow:0 12px 32px #769ab51c}
*{box-sizing:border-box}body{margin:0;background:linear-gradient(145deg,#e7f7ff 0%,#fff0f6 58%,#f8f3ff 100%);font-family:"Malgun Gothic","Apple SD Gothic Neo",system-ui,sans-serif;color:var(--ink);font-size:17px;line-height:1.65}
button{font:inherit;cursor:pointer;border:0}.app{max-width:960px;margin:0 auto;padding:24px 18px 54px}.top{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:18px}.brand{font-weight:900;letter-spacing:-.04em;font-size:clamp(18px,3vw,25px)}.pill{border-radius:99px;background:#ffffffb8;padding:7px 13px;font-size:13px;font-weight:800;color:#67819a}
.hero{text-align:center;padding:34px 20px 30px;border:2px solid #ffffffc9;border-radius:30px;background:linear-gradient(135deg,#d6f1ffdd,#ffe5efed);box-shadow:var(--shadow);position:relative;overflow:hidden}.hero:before,.hero:after{content:"✦";position:absolute;color:#fff;font-size:34px;opacity:.8}.hero:before{left:7%;top:13%}.hero:after{right:8%;bottom:12%}.eyebrow{display:inline-block;border-radius:99px;background:#fff;padding:5px 13px;font-size:13px;font-weight:900;color:#6586a2}.hero h1{font-size:clamp(30px,5.5vw,49px);line-height:1.22;letter-spacing:-.055em;margin:14px 0 12px}.hero p{max-width:600px;margin:0 auto;color:#5e6e84}.decor{font-size:28px;letter-spacing:8px;margin-top:16px}
.panel{margin-top:22px;background:#ffffffdf;border:1px solid #fff;border-radius:27px;padding:clamp(20px,4vw,38px);box-shadow:var(--shadow)}.hidden{display:none!important}.start{text-align:center}.start h2,.question h2{font-size:clamp(22px,4vw,30px);line-height:1.4;margin:0 0 10px;letter-spacing:-.035em}.start p{color:var(--muted);margin:0 auto 22px;max-width:610px}.primary{background:linear-gradient(100deg,#77c8eb,#f49abc);color:#263c52;font-weight:900;padding:14px 26px;border-radius:17px;box-shadow:0 7px 0 #b5dbea;transition:transform .15s,box-shadow .15s}.primary:hover{transform:translateY(-2px);box-shadow:0 9px 0 #b5dbea}.primary:active{transform:translateY(2px);box-shadow:0 3px 0 #b5dbea}.secondary{background:#eef8ff;border:1px solid #cceafa;color:#47657e;font-weight:800;padding:12px 20px;border-radius:15px}.progress-head{display:flex;justify-content:space-between;gap:10px;align-items:center;font-weight:900;font-size:14px;margin-bottom:10px}.track{height:12px;border-radius:99px;background:#edf0f7;overflow:hidden;margin-bottom:28px}.fill{height:100%;width:0;background:linear-gradient(90deg,#75c9ec,#f59bbd);border-radius:99px;transition:width .25s}.qtag{font-size:13px;font-weight:900;color:#d879a1;margin-bottom:8px}.question h2{margin-bottom:22px}.choices{display:grid;gap:12px}.choice{display:flex;align-items:center;gap:13px;text-align:left;width:100%;background:#fff;border:2px solid #e5eef6;border-radius:18px;padding:15px 17px;min-height:68px;color:var(--ink);transition:.15s}.choice:hover{border-color:#a9dff5;background:#f6fcff;transform:translateY(-1px)}.choice.selected{border-color:#f1a1c0;background:#fff2f7;box-shadow:0 0 0 3px #ffe4ee}.letter{display:grid;place-items:center;flex:0 0 36px;width:36px;height:36px;border-radius:12px;background:#e3f5ff;font-weight:900;color:#5786a3}.choice:nth-child(2) .letter{background:#ffe8f0;color:#c76c91}.choice:nth-child(3) .letter{background:#f0eaff;color:#8871b9}.nav{display:flex;justify-content:space-between;gap:12px;margin-top:24px}.nav button{min-width:115px}.hint{font-size:13px;color:#7c8797;margin-top:15px}
.result-head{text-align:center}.type-label{display:inline-block;padding:7px 17px;background:#fff0f6;color:#c45e89;border-radius:99px;font-weight:900;letter-spacing:.08em}.result-head h2{font-size:clamp(30px,5vw,42px);letter-spacing:-.04em;line-height:1.2;margin:14px 0 6px}.result-head p{color:var(--muted);margin:0}.pokemon-card{margin:24px auto 0;max-width:700px;border-radius:28px;padding:24px;background:linear-gradient(145deg,#e1f5ff,#ffebf2);border:1px solid white;text-align:center}.art-wrap{width:min(280px,75vw);height:240px;margin:0 auto 12px;display:grid;place-items:center;position:relative}.art{width:100%;height:100%;object-fit:contain;filter:drop-shadow(0 10px 9px #6d89a22a)}.art-fallback{display:none;font-size:15px;color:#75849a;background:#ffffffb5;padding:12px;border-radius:12px}.poke-name{font-size:clamp(28px,5vw,38px);font-weight:950;letter-spacing:-.04em;margin:0}.species{color:#60758b;font-size:14px;font-weight:800;margin:5px 0 13px}.types{display:flex;gap:7px;justify-content:center;flex-wrap:wrap}.type-chip{padding:4px 12px;border-radius:99px;background:#fff;font-size:13px;font-weight:900;color:#52718c}.description{max-width:600px;margin:18px auto 0;font-size:17px}.subheading{font-size:21px;font-weight:950;letter-spacing:-.03em;margin:0 0 12px}.reason-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px}.reason{background:#f4fbff;border:1px solid #e1f1fa;border-radius:19px;padding:18px}.reason:nth-child(2){background:#fff5f8;border-color:#ffe5ee}.reason p{margin:0;color:#56677e}.compat{display:flex;align-items:center;gap:20px;background:linear-gradient(110deg,#e7f7ff,#fff0f6);padding:20px;border-radius:22px}.compat .art-wrap{width:145px;height:135px;flex:0 0 145px;margin:0}.compat h3{font-size:24px;margin:5px 0}.compat p{margin:0;color:#56677e}.notice{font-size:13px;color:#7b8797;text-align:center;margin:17px 0 0}.actions{text-align:center;margin-top:24px}.foot{text-align:center;color:#8591a2;font-size:12px;margin-top:24px}
@media(max-width:620px){.app{padding:14px 12px 35px}.hero{padding:27px 15px}.panel{padding:19px 15px}.reason-grid{grid-template-columns:1fr}.compat{gap:10px;padding:13px}.compat .art-wrap{width:105px;height:110px;flex-basis:105px}.compat h3{font-size:20px}.choice{padding:12px;min-height:62px}.nav button{min-width:0;flex:1}.top{align-items:flex-start}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
</style>
</head>
<body>
<main class="app">
  <header class="top"><div class="brand">☁️ 포켓몬 MBTI 연구소</div><div class="pill">나만의 포켓몬 찾기 ✨</div></header>
  <section class="hero" aria-labelledby="main-title">
    <div class="eyebrow">MY LITTLE POKÉMON MATCH</div>
    <h1 id="main-title">MBTI로 포켓몬 찾기!</h1>
    <p>나의 성격과 꼭 닮은 포켓몬은 누구일까요?<br>12개의 질문에 편하게 답하고 나만의 포켓몬 친구를 만나 봐요.</p>
    <div class="decor" aria-hidden="true">☁️ 💗 ⭐ 🌸</div>
  </section>
  <section id="intro" class="panel start">
    <h2>준비됐나요, 트레이너? 🌈</h2>
    <p>정답은 없어요! 평소의 나와 더 가까운 선택지를 골라 주세요. 잘 모르겠다면 언제든 <b>“잘 모르겠음 🤔”</b>을 선택해도 괜찮아요.</p>
    <button id="startBtn" class="primary" type="button">내 포켓몬 찾으러 가기 💫</button>
    <p class="hint">약 2~3분 · 12문항 · 결과는 재미로 즐겨 주세요!</p>
  </section>
  <section id="quiz" class="panel question hidden" aria-live="polite">
    <div class="progress-head"><span id="stepLabel">QUESTION 01 / 12</span><span id="percent">0%</span></div>
    <div class="track" role="progressbar" aria-label="검사 진행률" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" id="progress"><div id="progressFill" class="fill"></div></div>
    <div id="qTag" class="qtag">QUESTION 01</div>
    <h2 id="questionText">질문</h2>
    <div id="choices" class="choices"></div>
    <div class="nav"><button id="prevBtn" class="secondary" type="button">← 이전</button><button id="nextBtn" class="primary" type="button" disabled>다음 질문 →</button></div>
    <div class="hint">마음이 정해지지 않았다면 “잘 모르겠음 🤔”도 좋은 답이에요.</div>
  </section>
  <section id="results" class="panel hidden" aria-live="polite"></section>
  <footer class="foot">팬을 위한 비공식 성격 테스트 · Pokémon 및 관련 캐릭터는 각 권리자에게 권리가 있습니다.</footer>
</main>
<script>
"use strict";
const QUESTIONS = [
 {q:"친구들과 신나는 하루를 보낸 뒤 나는…",a:["에너지가 충전돼서 더 이야기하고 싶어!","혼자 조용히 쉬면서 에너지를 채우고 싶어.","잘 모르겠음 🤔"],d:0},
 {q:"새로운 모임에 갔을 때 나는 보통…",a:["먼저 말을 걸고 분위기를 이끌어.","천천히 살펴보고 편한 사람과 이야기해.","잘 모르겠음 🤔"],d:0},
 {q:"생각이 떠오르면 나는…",a:["말하면서 생각을 정리하는 편이야.","속으로 충분히 생각한 뒤 말하는 편이야.","잘 모르겠음 🤔"],d:0},
 {q:"여행 계획을 세울 때 더 끌리는 건…",a:["직접 보고 느낄 수 있는 현실적인 경험!","상상력을 자극하는 새로운 가능성과 아이디어!","잘 모르겠음 🤔"],d:1},
 {q:"설명서를 읽을 때 나는…",a:["구체적인 사실과 순서를 확인해.","전체적인 의미와 숨은 가능성을 먼저 떠올려.","잘 모르겠음 🤔"],d:1},
 {q:"이야기를 들을 때 더 기억에 남는 건…",a:["실제로 있었던 일과 자세한 정보","그 일이 의미하는 것과 앞으로의 가능성","잘 모르겠음 🤔"],d:1},
 {q:"친구가 고민을 털어놓으면 나는…",a:["문제를 해결할 수 있는 방법을 같이 찾아봐.","먼저 마음을 이해하고 따뜻하게 공감해 줘.","잘 모르겠음 🤔"],d:2},
 {q:"중요한 결정을 할 때 더 우선하는 건…",a:["논리와 객관적인 기준이야.","사람들의 마음과 내가 중요하게 여기는 가치야.","잘 모르겠음 🤔"],d:2},
 {q:"의견이 서로 다를 때 나는…",a:["무엇이 합리적인지 차분히 따져 봐.","서로 상처받지 않도록 배려하며 조율해.","잘 모르겠음 🤔"],d:2},
 {q:"과제를 시작할 때 나는…",a:["계획을 세우고 차근차근 끝내는 게 좋아.","상황에 맞춰 유연하게 진행하는 게 좋아.","잘 모르겠음 🤔"],d:3},
 {q:"약속이나 일정이 생기면 나는…",a:["미리 정해 두면 마음이 편안해.","그날의 기분과 상황에 따라 정하는 게 좋아.","잘 모르겠음 🤔"],d:3},
 {q:"마감일이 다가오면 나는…",a:["여유 있게 미리 끝내 두고 싶어.","마지막 순간의 집중력으로 해내는 편이야.","잘 모르겠음 🤔"],d:3}
];
// Every type has a Pokémon, Korean name, category, elemental types, artwork ID,
// personality copy, reasons, and one compatibility recommendation.
const DATA = {
 ISTJ:{name:"망나뇽",id:149,cat:"드래곤 포켓몬",types:["드래곤","비행"],desc:"믿음직하고 책임감이 강한 당신. 한 번 맡은 일은 끝까지 해내는 든든한 수호자예요.",r:["차근차근 계획을 세우고 약속을 지키는 모습이 성실한 망나뇽과 닮았어요.","말보다 행동으로 믿음을 주고, 소중한 사람을 꾸준히 지켜 주는 타입이에요."],match:"ENFP",why:"당신의 안정감에 ENFP의 밝은 호기심과 즉흥성이 더해지면, 서로의 세계를 넓혀 주는 팀이 될 수 있어요."},
 ISFJ:{name:"푸린",id:39,cat:"풍선 포켓몬",types:["노말","페어리"],desc:"주변을 세심하게 살피고 따뜻하게 챙기는 다정한 사람. 당신 곁에서는 누구나 편안함을 느껴요.",r:["상대의 기분을 잘 알아차리고 조용히 도와주는 다정함이 푸린을 떠올리게 해요.","소중한 사람을 기억하고 꾸준히 마음을 표현하는 점도 꼭 닮았어요."],match:"ESFP",why:"당신의 배려와 ESFP의 활기찬 에너지가 만나면, 편안함과 즐거움을 함께 나눌 수 있어요."},
 INFJ:{name:"루카리오",id:448,cat:"파동 포켓몬",types:["격투","강철"],desc:"사람의 마음을 깊이 이해하고 자신만의 신념을 소중히 여겨요. 조용하지만 강한 내면을 가진 타입이에요.",r:["겉으로 드러나지 않는 마음과 분위기를 읽으려는 통찰력이 루카리오와 닮았어요.","중요한 가치가 생기면 진심을 다해 지키는 모습이 인상적이에요."],match:"ENTP",why:"당신의 깊이 있는 통찰과 ENTP의 새로운 발상이 만나면, 서로의 생각을 자극하는 특별한 대화가 펼쳐져요."},
 INTJ:{name:"뮤츠",id:150,cat:"유전자 포켓몬",types:["에스퍼"],desc:"큰 그림을 보고 전략적으로 움직이는 독립적인 탐구자. 복잡한 문제도 자신만의 방식으로 풀어가요.",r:["가능성을 분석하고 효율적인 전략을 세우는 모습이 뮤츠의 지적인 이미지와 어울려요.","혼자 깊이 생각하며 스스로 납득할 때까지 파고드는 편이에요."],match:"ENFP",why:"당신의 전략적인 시선에 ENFP의 상상력과 따뜻한 열정이 더해져 새로운 가능성을 발견할 수 있어요."},
 ISTP:{name:"메타그로스",id:376,cat:"철발톱 포켓몬",types:["강철","에스퍼"],desc:"침착하고 실용적인 문제 해결사. 복잡한 상황에서도 핵심을 파악하고 직접 부딪쳐 해결하는 편이에요.",r:["관찰하고 분석한 뒤 가장 실용적인 해결책을 찾는 점이 메타그로스와 닮았어요.","필요할 때 빠르게 행동하고, 독립적으로 문제를 다루는 데 강점이 있어요."],match:"ESFJ",why:"당신의 차분한 판단과 ESFJ의 따뜻한 협동심이 어우러지면, 실력과 팀워크를 모두 살릴 수 있어요."},
 ISFP:{name:"이브이",id:133,cat:"진화 포켓몬",types:["노말"],desc:"부드러운 감성과 자신만의 취향을 가진 자유로운 영혼. 작은 순간에서도 아름다움을 발견해요.",r:["자신만의 속도로 가능성을 탐색하고 개성을 자연스럽게 드러내는 점이 이브이와 닮았어요.","말보다 경험과 감각으로 세상을 느끼며, 따뜻한 진심을 소중히 여겨요."],match:"ENFJ",why:"당신의 섬세한 감각과 ENFJ의 따뜻한 응원이 만나면, 서로의 장점을 발견하고 성장하도록 도와줘요."},
 INFP:{name:"세레비",id:251,cat:"시간이동 포켓몬",types:["에스퍼","풀"],desc:"상상력이 풍부하고 마음속의 소중한 가치를 지키는 이상주의자. 다정한 시선으로 세상을 바라봐요.",r:["더 나은 세상을 상상하고 작은 생명과 마음을 소중히 여기는 점이 세레비와 어울려요.","자기만의 내면 세계가 풍부하고 진심이 통하는 관계를 중요하게 생각해요."],match:"ENTJ",why:"당신의 상상력과 ENTJ의 추진력이 만나면, 마음속 아이디어를 현실의 변화로 만들어 갈 수 있어요."},
 INTP:{name:"폴리곤",id:137,cat:"가상 포켓몬",types:["노말"],desc:"호기심이 많고 논리적으로 탐구하는 생각 수집가. 당연해 보이는 것도 한 번 더 질문해요.",r:["원리를 이해하고 새로운 방식으로 문제를 바라보는 분석력이 폴리곤과 잘 맞아요.","혼자 몰입해 관심 분야를 깊이 탐구하는 시간이 큰 즐거움이에요."],match:"ENTJ",why:"당신의 독창적인 분석과 ENTJ의 실행력이 힘을 합치면, 아이디어를 실제 성과로 연결하기 좋아요."},
 ESTP:{name:"갸라도스",id:130,cat:"흉악 포켓몬",types:["물","비행"],desc:"대담하고 행동력이 넘치는 모험가. 망설이기보다 직접 뛰어들어 경험하며 길을 찾아요.",r:["눈앞의 상황을 빠르게 파악하고 과감하게 움직이는 에너지가 갸라도스와 닮았어요.","예상 밖의 순간에도 기회를 포착하고 실전에서 해결책을 찾는 편이에요."],match:"ISFJ",why:"당신의 대담함과 ISFJ의 세심함이 균형을 이루면, 도전은 더 안전하고 관계는 더 든든해져요."},
 ESFP:{name:"피카츄",id:25,cat:"쥐 포켓몬",types:["전기"],desc:"밝은 에너지로 주변을 환하게 만드는 분위기 메이커. 지금 이 순간을 즐기고 사람들과 기쁨을 나눠요.",r:["사람들과 함께 즐거움을 나누고 생생한 경험을 좋아하는 점이 피카츄와 닮았어요.","표현이 솔직하고 따뜻해서 주변 사람들에게 활기를 전해요."],match:"ISFJ",why:"당신의 밝은 추진력에 ISFJ의 안정적인 배려가 더해지면, 즐거움과 편안함을 함께 만들 수 있어요."},
 ENFP:{name:"파치리스",id:417,cat:"전기다람쥐 포켓몬",types:["전기"],desc:"호기심과 아이디어가 톡톡 튀는 낙천가. 사람과 가능성을 발견하는 걸 좋아하는 에너지 넘치는 타입이에요.",r:["새로운 만남과 아이디어에 쉽게 설레고 주변에 긍정적인 기운을 전해요.","정해진 틀보다는 다양한 가능성을 열어 두고 자유롭게 탐험하는 편이에요."],match:"ISTJ",why:"당신의 유연한 상상력과 ISTJ의 꾸준한 실행력이 만나면, 좋은 아이디어를 차근차근 현실로 만들 수 있어요."},
 ENTP:{name:"겟핸보숭",id:424,cat:"긴꼬리 포켓몬",types:["노말"],desc:"재치 있고 아이디어가 풍부한 토론가. 익숙한 방식에 질문을 던지고 새로운 가능성을 찾아요.",r:["다른 관점에서 생각하고 아이디어를 주고받는 걸 즐기는 점이 잘 어울려요.","빠르게 연결점을 찾고 재미있는 실험을 시도하는 호기심이 강해요."],match:"INFJ",why:"당신의 발랄한 발상과 INFJ의 깊은 통찰이 만나면, 흥미로운 아이디어가 의미 있는 방향으로 발전해요."},
 ESTJ:{name:"괴력몬",id:68,cat:"괴력 포켓몬",types:["격투"],desc:"목표를 분명히 세우고 사람들을 이끄는 실천가. 책임감과 추진력으로 일을 끝까지 완수해요.",r:["역할을 정리하고 목표를 향해 효율적으로 움직이는 점이 괴력몬의 힘과 어울려요.","결정이 필요할 때 주도적으로 나서고 결과를 만들어 내는 편이에요."],match:"ISFP",why:"당신의 추진력에 ISFP의 섬세한 감각과 유연함이 더해지면, 목표와 사람의 마음을 함께 살필 수 있어요."},
 ESFJ:{name:"토게키스",id:468,cat:"축복 포켓몬",types:["페어리","비행"],desc:"사람들을 연결하고 모두가 편안하도록 돕는 다정한 조율자. 함께하는 기쁨을 중요하게 여겨요.",r:["주변 사람들을 챙기고 좋은 분위기를 만들려는 마음이 토게키스와 닮았어요.","협력과 따뜻한 표현으로 관계를 더욱 튼튼하게 만드는 타입이에요."],match:"ISTP",why:"당신의 사교적인 배려와 ISTP의 침착한 실용성이 만나면, 서로 다른 방식으로 문제를 보완할 수 있어요."},
 ENFJ:{name:"가디안",id:282,cat:"포옹 포켓몬",types:["에스퍼","페어리"],desc:"사람의 가능성을 믿고 진심으로 응원하는 리더. 따뜻한 공감과 비전으로 함께 성장하도록 이끌어요.",r:["상대의 장점을 발견하고 진심으로 응원하는 모습이 가디안의 수호 이미지와 어울려요.","공동의 목표를 위해 사람들을 연결하고 마음을 모으는 데 강점이 있어요."],match:"ISFP",why:"당신의 따뜻한 리더십과 ISFP의 진솔한 감성이 만나면, 서로의 개성을 존중하며 함께 성장할 수 있어요."},
 ENTJ:{name:"리자몽",id:6,cat:"화염 포켓몬",types:["불꽃","비행"],desc:"큰 목표를 향해 자신 있게 나아가는 전략가. 도전 앞에서 주도권을 잡고 길을 개척해요.",r:["목표를 세우고 자원을 모아 실행하는 추진력이 리자몽의 당당한 에너지와 닮았어요.","어려운 과제도 성장 기회로 보고 결단력 있게 도전하는 편이에요."],match:"INFP",why:"당신의 현실적인 추진력과 INFP의 가치 중심 상상력이 만나면, 성과에 의미와 따뜻함을 더할 수 있어요."}
};
const DIMS = [["E","I"],["S","N"],["T","F"],["J","P"]];
const KEYS = ["EI","SN","TF","JP"];
const KOREAN = {E:"외향",I:"내향",S:"감각",N:"직관",T:"사고",F:"감정",J:"판단",P:"인식"};
let index=0, answers=Array(QUESTIONS.length).fill(null), finished=false;
const $ = id => document.getElementById(id);
const intro=$("intro"), quiz=$("quiz"), results=$("results");
function show(section){[intro,quiz,results].forEach(el=>el.classList.add("hidden"));section.classList.remove("hidden");}
function progress(){const done=answers.filter(v=>v!==null).length;const pct=Math.round(done/QUESTIONS.length*100);$("progressFill").style.width=pct+"%";$("progress").setAttribute("aria-valuenow",String(pct));$("percent").textContent=pct+"%";$("stepLabel").textContent=`QUESTION ${String(index+1).padStart(2,"0")} / ${QUESTIONS.length}`;}
function renderQuestion(){
 const item=QUESTIONS[index];$("qTag").textContent=`QUESTION ${String(index+1).padStart(2,"0")}`;
 $("questionText").textContent=item.q;$("choices").replaceChildren();
 item.a.forEach((label,i)=>{const b=document.createElement("button");b.type="button";b.className="choice"+(answers[index]===i?" selected":"");b.setAttribute("aria-pressed",answers[index]===i?"true":"false");const letter=document.createElement("span");letter.className="letter";letter.textContent=["A","B","🤔"][i];const txt=document.createElement("span");txt.textContent=label;b.append(letter,txt);b.addEventListener("click",()=>{answers[index]=i;renderQuestion();});$("choices").appendChild(b);});
 $("prevBtn").disabled=index===0;$("prevBtn").style.opacity=index===0?".45":"1";
 $("nextBtn").disabled=answers[index]===null;$("nextBtn").textContent=index===QUESTIONS.length-1?"결과 확인하기 ✨":"다음 질문 →";
 progress();
}
function calculate(){
 const counts={E:0,I:0,S:0,N:0,T:0,F:0,J:0,P:0};
 answers.forEach((answer,qi)=>{if(answer===null||answer===2)return;const dimension=QUESTIONS[qi].d;counts[DIMS[dimension][answer]]++;});
 // Stable tie-break: first letter of each dimension (E, S, T, J) wins ties.
 return KEYS.map((key,dim)=>{const [first,second]=DIMS[dim];return counts[first]>=counts[second]?first:second;}).join("");
}
function artwork(id,name,extraClass=""){
 const wrap=document.createElement("div");wrap.className="art-wrap"+(extraClass?" "+extraClass:"");
 const img=document.createElement("img");img.className="art";img.alt=name+" 공식 스타일 포켓몬 아트워크";img.loading="eager";img.src=`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/${id}.png`;
 const fallback=document.createElement("div");fallback.className="art-fallback";fallback.textContent="이미지를 불러오지 못했어요. 인터넷 연결을 확인해 주세요.";
 img.addEventListener("error",()=>{img.style.display="none";fallback.style.display="block";});
 wrap.append(img,fallback);return wrap;
}
function make(tag,cls,text){const el=document.createElement(tag);if(cls)el.className=cls;if(text!==undefined)el.textContent=text;return el;}
function renderResults(type){
 const p=DATA[type], partner=DATA[p.match];results.replaceChildren();
 const head=make("div","result-head");head.append(make("span","type-label",type+" TYPE"),make("h2","","당신과 닮은 포켓몬은…"),make("p","","성격 유형을 바탕으로 찾아본 나만의 포켓몬 친구!"));results.append(head);
 const card=make("article","pokemon-card");card.append(artwork(p.id,p.name),make("h3","poke-name",p.name),make("p","species",p.cat));
 const chips=make("div","types");p.types.forEach(t=>chips.append(make("span","type-chip",t+" 타입")));card.append(chips,make("p","description",p.desc));results.append(card);
 const reasons=make("section","");reasons.style.marginTop="25px";reasons.append(make("h3","subheading","💗 이런 점이 닮았어요"));
 const grid=make("div","reason-grid");p.r.forEach((reason,i)=>{const r=make("article","reason");r.append(make("p","",`${i+1}. ${reason}`));grid.append(r);});reasons.append(grid);results.append(reasons);
 const comp=make("section","");comp.style.marginTop="28px";comp.append(make("h3","subheading","🌈 잘 맞을 것 같은 포켓몬 친구"));
 const cbox=make("div","compat");cbox.append(artwork(partner.id,partner.name),make("div","",""));
 const textBox=cbox.lastChild;textBox.append(make("span","type-label",p.match+" TYPE"),make("h3","",partner.name),make("p","",p.why));comp.append(cbox,make("p","notice","궁합은 재미로 보는 추천이에요. 실제 관계는 서로를 알아 가는 과정이 더 중요해요."));results.append(comp);
 const note=make("p","notice","포켓몬 아트워크는 외부 이미지 서버에서 불러옵니다. 이미지를 보려면 인터넷 연결이 필요하며, 연결이 없거나 이미지 서버에 접근할 수 없으면 안내 문구가 표시됩니다.");results.append(note);
 const actions=make("div","actions");const reset=make("button","primary","다시 검사하기 🔄");reset.type="button";reset.addEventListener("click",resetQuiz);actions.append(reset);results.append(actions);
 show(results);window.scrollTo({top:0,behavior:"smooth"});
}
function resetQuiz(){index=0;answers=Array(QUESTIONS.length).fill(null);finished=false;show(intro);progress();window.scrollTo({top:0,behavior:"smooth"});}
$("startBtn").addEventListener("click",()=>{index=0;show(quiz);renderQuestion();window.scrollTo({top:0,behavior:"smooth"});});
$("prevBtn").addEventListener("click",()=>{if(index>0){index--;renderQuestion();}});
$("nextBtn").addEventListener("click",()=>{if(answers[index]===null)return;if(index<QUESTIONS.length-1){index++;renderQuestion();}else{finished=true;renderResults(calculate());}});
progress();
</script>
</body>
</html>
"""

components.html(HTML, height=2200, scrolling=True)
