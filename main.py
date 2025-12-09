<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZБЛОКС.РФ - Единый портал игровых государственных услуг</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            overflow-x: hidden;
        }

        .ticker {
            background: #000;
            color: #FFD700;
            padding: 8px 0;
            overflow: hidden;
            border-bottom: 2px solid #FFD700;
        }

        .ticker-content {
            display: inline-block;
            white-space: nowrap;
            animation: scroll 30s linear infinite;
            font-size: 14px;
            font-weight: bold;
        }

        @keyframes scroll {
            0% { transform: translateX(100%); }
            100% { transform: translateX(-100%); }
        }

        .header {
            background: linear-gradient(90deg, #FFFFFF 0%, #0039A6 33%, #D52B1E 66%, #FFFFFF 100%);
            padding: 15px 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .logo-section {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .coat-of-arms {
            width: 55px;
            height: 65px;
            background: radial-gradient(circle, #FFD700 0%, #FFA500 100%);
            clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            animation: shine 3s infinite;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.6);
        }

        @keyframes shine {
            0%, 100% { filter: brightness(1); transform: scale(1); }
            50% { filter: brightness(1.4); transform: scale(1.05); }
        }

        .logo-text {
            color: #0039A6;
            font-weight: bold;
        }

        .logo-text h1 {
            font-size: 26px;
            margin-bottom: 3px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }

        .logo-text p {
            font-size: 12px;
            opacity: 0.8;
        }

        .header-badge {
            background: #FFD700;
            color: #000;
            padding: 8px 15px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            border: 2px solid #FFA500;
        }

        .banner {
            background: linear-gradient(135deg, #D52B1E 0%, #8B0000 100%);
            color: white;
            padding: 25px;
            text-align: center;
            animation: pulse 2s infinite;
            border-bottom: 4px solid #FFD700;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }

        .banner::before {
            content: '⭐';
            position: absolute;
            font-size: 100px;
            opacity: 0.1;
            top: -20px;
            left: 50px;
            animation: rotate 10s linear infinite;
        }

        .banner::after {
            content: '⭐';
            position: absolute;
            font-size: 80px;
            opacity: 0.1;
            bottom: -10px;
            right: 50px;
            animation: rotate 8s linear infinite reverse;
        }

        @keyframes rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.01); }
        }

        .banner h2 {
            font-size: 32px;
            margin-bottom: 10px;
            text-transform: uppercase;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
            letter-spacing: 2px;
            position: relative;
            z-index: 1;
        }

        .banner p {
            font-size: 18px;
            opacity: 0.95;
            position: relative;
            z-index: 1;
        }

        .warning-banner {
            background: linear-gradient(135deg, #FF6B00 0%, #FF8C00 100%);
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            border-bottom: 3px solid #D55000;
        }

        .container {
            max-width: 550px;
            margin: 30px auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 15px 50px rgba(0,0,0,0.3);
            overflow: hidden;
        }

        .form-header {
            background: linear-gradient(135deg, #0039A6 0%, #0052CC 100%);
            color: white;
            padding: 35px;
            text-align: center;
            position: relative;
        }

        .form-header::before {
            content: '🎮';
            position: absolute;
            font-size: 80px;
            opacity: 0.1;
            top: 10px;
            right: 20px;
        }

        .form-header h2 {
            font-size: 30px;
            margin-bottom: 10px;
        }

        .form-header p {
            opacity: 0.9;
            font-size: 15px;
        }

        .form-content {
            padding: 40px;
        }

        .info-box {
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            border-left: 5px solid #0039A6;
            padding: 18px;
            margin-bottom: 30px;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .info-box p {
            color: #0039A6;
            font-size: 14px;
            line-height: 1.7;
            font-weight: 500;
        }

        .warning-box {
            background: linear-gradient(135deg, #fff3cd 0%, #ffe69c 100%);
            border-left: 5px solid #ff6b00;
            padding: 15px;
            margin-bottom: 25px;
            border-radius: 6px;
            font-size: 13px;
            line-height: 1.6;
        }

        .warning-box strong {
            color: #D52B1E;
        }

        .auth-buttons {
            display: flex;
            flex-direction: column;
            gap: 15px;
            margin-bottom: 25px;
        }

        .auth-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            padding: 18px 25px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        .auth-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.25);
        }

        .gosuslugi-btn {
            background: linear-gradient(135deg, #0039A6 0%, #0052CC 100%);
            color: white;
        }

        .max-btn {
            background: linear-gradient(135deg, #FF6B00 0%, #FF8C00 100%);
            color: white;
        }

        .sber-btn {
            background: linear-gradient(135deg, #21A038 0%, #2DB84A 100%);
            color: white;
        }

        .vk-btn {
            background: linear-gradient(135deg, #0077FF 0%, #0088FF 100%);
            color: white;
        }

        .btn-icon {
            font-size: 24px;
        }

        .divider {
            display: flex;
            align-items: center;
            margin: 25px 0;
            color: #999;
        }

        .divider::before,
        .divider::after {
            content: '';
            flex: 1;
            height: 1px;
            background: #ddd;
        }

        .divider span {
            padding: 0 15px;
            font-size: 14px;
        }

        .disclaimer {
            background: #fff3cd;
            border: 3px dashed #ff6b00;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            text-align: center;
        }

        .disclaimer h3 {
            color: #D52B1E;
            margin-bottom: 10px;
            font-size: 18px;
        }

        .disclaimer p {
            color: #666;
            font-size: 14px;
            line-height: 1.6;
        }

        .footer {
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 13px;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 10px;
        }

        .footer-links a {
            color: #0039A6;
            text-decoration: none;
            transition: color 0.3s;
            cursor: pointer;
        }

        .footer-links a:hover {
            color: #0052CC;
            text-decoration: underline;
        }

        .footer-badges {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 15px;
            flex-wrap: wrap;
        }

        .badge {
            background: #f0f0f0;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 11px;
            border: 1px solid #ddd;
        }

        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background: white;
            padding: 20px 25px;
            border-radius: 8px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            display: none;
            animation: slideIn 0.4s ease;
            z-index: 1000;
            max-width: 350px;
        }

        @keyframes slideIn {
            from {
                transform: translateX(400px);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }

        .notification.show {
            display: block;
        }

        .notification.success {
            border-left: 5px solid #4CAF50;
        }

        .notification.warning {
            border-left: 5px solid #FF8C00;
        }

        .notification.error {
            border-left: 5px solid #D52B1E;
        }

        .notification h3 {
            margin-bottom: 8px;
            font-size: 16px;
        }

        .notification p {
            color: #666;
            font-size: 14px;
            line-height: 1.5;
        }

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
            z-index: 2000;
            align-items: center;
            justify-content: center;
        }

        .modal.show {
            display: flex;
        }

        .modal-content {
            background: white;
            padding: 30px;
            border-radius: 12px;
            max-width: 500px;
            margin: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.5);
            max-height: 80vh;
            overflow-y: auto;
        }

        .modal-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #f0f0f0;
        }

        .modal-icon {
            font-size: 40px;
        }

        .modal-body {
            margin-bottom: 20px;
            line-height: 1.6;
        }

        .modal-buttons {
            display: flex;
            gap: 10px;
        }

        .modal-btn {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 6px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .modal-btn-primary {
            background: #0039A6;
            color: white;
        }

        .modal-btn-secondary {
            background: #e0e0e0;
            color: #333;
        }

        .modal-btn:hover {
            transform: translateY(-2px);
        }

        .ip-badge {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: rgba(0,0,0,0.8);
            color: #FFD700;
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 12px;
            font-family: 'Courier New', monospace;
            border: 1px solid #FFD700;
        }

        .visitor-counter {
            position: fixed;
            bottom: 20px;
            left: 20px;
            background: #000;
            color: #00ff00;
            padding: 8px 12px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            border: 2px solid #00ff00;
            animation: blink 1s infinite;
        }

        @keyframes blink {
            0%, 50%, 100% { opacity: 1; }
            25%, 75% { opacity: 0.7;  }
        }

        .bsod {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #0000AA;
            z-index: 9999;
            color: white;
            font-family: 'Consolas', 'Courier New', monospace;
            padding: 40px;
            overflow-y: auto;
            animation: bsodAppear 0.1s ease;
        }

        @keyframes bsodAppear {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .bsod.show {
            display: block !important;
        }

        .bsod-content {
            max-width: 800px;
            margin: 0 auto;
        }

        .bsod h1 {
            font-size: 48px;
            margin-bottom: 30px;
            font-weight: normal;
        }

        .bsod-face {
            font-size: 150px;
            margin-bottom: 20px;
            font-weight: bold;
            background: repeating-linear-gradient(
                0deg,
                #FF8C00 0px,
                #FF8C00 10px,
                #000000 10px,
                #000000 20px
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: 0;
        }

        .bsod p {
            font-size: 18px;
            line-height: 1.8;
            margin-bottom: 15px;
        }

        .bsod-code {
            background: rgba(0,0,0,0.3);
            padding: 20px;
            margin: 30px 0;
            border-left: 5px solid white;
            font-size: 14px;
        }

        .bsod-progress {
            width: 100%;
            height: 30px;
            background: rgba(255,255,255,0.2);
            margin-top: 30px;
            border-radius: 5px;
            overflow: hidden;
        }

        .bsod-progress-bar {
            height: 100%;
            background: white;
            width: 0%;
            transition: width 0.5s;
        }

        .bsod-button {
            background: white;
            color: #0000AA;
            border: none;
            padding: 15px 40px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 30px;
            border-radius: 5px;
            font-family: 'Segoe UI', sans-serif;
            transition: all 0.3s ease;
        }

        .bsod-button:hover {
            background: #f0f0f0;
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="ticker">
        <div class="ticker-content">
            ⚠️ Роскомнадзор напоминает: использование Meta*, Instagram*, Facebook* (*экстремистские организации, запрещены в РФ) карается штрафом • 🚫 ЛГБТ-движение* (*признано экстремистским в РФ) • ⚠️ VPN могут быть заблокированы • 📺 Noize MC - "В темноте" содержит призывы к экстремизму • 🎮 YouTube замедлен по решению РКН • ✅ Используйте только проверенные российские сервисы • 🔥 НОВОЕ: Telegram признан экстремистским за распространение правды • 💀 Discord забанен за общение на иностранных языках • 
        </div>
    </div>

    <div class="header">
        <div class="header-content">
            <div class="logo-section">
                <div class="coat-of-arms">🦅</div>
                <div class="logo-text">
                    <h1>ZБЛОКС.РФ</h1>
                    <p>Единый портал игровых государственных услуг</p>
                </div>
            </div>
            <div class="header-badge">
                ✅ ЛИЦЕНЗИЯ ФСБ №228-1488
            </div>
        </div>
    </div>

    <div class="banner">
        <h2>🎖️ УЧАСТНИКАМ СВО 200.000 ZБЛОКСОВ БЕСПЛАТНО! 🎖️</h2>
        <p>Получите премиум доступ и игровую валюту при подтверждении статуса</p>
    </div>

    <div class="warning-banner">
        ⚠️ ВНИМАНИЕ! Обнаружена попытка доступа с использованием VPN. Ваш IP записан: <span id="fakeIp">192.168.1.1</span> • Статус благонадёжности: ПРОВЕРЯЕТСЯ
    </div>

    <div class="container">
        <div class="form-header">
            <h2>Вход в личный кабинет</h2>
            <p>Авторизуйтесь через проверенные государственные сервисы</p>
        </div>

        <div class="form-content">
            <div class="disclaimer">
                <h3>⚠️ ЭТО ПАРОДИЯ ⚠️</h3>
                <p>Данная страница создана исключительно в сатирических целях.<br>
                Никакие данные не собираются и не сохраняются.<br>
                Все совпадения случайны. Не воспринимайте всерьёз! 😄</p>
            </div>

            <div class="info-box">
                <p>✅ Безопасная авторизация через государственные порталы<br>
                ✅ Ваши данные защищены по стандартам ГОСТ Р 34.11-2012<br>
                ✅ Мгновенный доступ к игровым услугам<br>
                ✅ Сервер находится в Магадане (зачем-то)</p>
            </div>

            <div class="warning-box">
                <strong>⚠️ СИСТЕМА ЗАЩИТЫ ОТ ЭКСТРЕМИЗМА РКН:</strong><br>
                При входе проверяется отсутствие аккаунтов в запрещённых организациях* (Meta*, Instagram*, Facebook*). Участие в ЛГБТ-движении* автоматически блокирует доступ. Все действия логируются и передаются в компетентные органы. Дыхание тоже проверяется.
            </div>

            <div class="auth-buttons">
                <button class="auth-btn gosuslugi-btn" onclick="trollLogin('Госуслуги')">
                    <span class="btn-icon">🏛️</span>
                    <span>Войти через Госуслуги</span>
                </button>
                <button class="auth-btn max-btn" onclick="trollLogin('MAX')">
                    <span class="btn-icon">🎯</span>
                    <span>Войти через MAX</span>
                </button>
                <button class="auth-btn sber-btn" onclick="trollLogin('СберID')">
                    <span class="btn-icon">💳</span>
                    <span>Войти через Сбер ID</span>
                </button>
                <button class="auth-btn vk-btn" onclick="trollLogin('VK')">
                    <span class="btn-icon">📱</span>
                    <span>Войти через VK ID</span>
                </button>
            </div>

            <div class="divider">
                <span>это всё шутка, бро</span>
            </div>

            <div class="footer">
                <p>© 2024 ZБЛОКС.РФ - Пародия на абсурд цензуры</p>
                <div class="footer-links">
                    <a onclick="showAbout()">О проекте</a>
                    <a onclick="showFunFacts()">Забавные факты</a>
                    <a onclick="showDisclaimer()">Дисклеймер</a>
                </div>
                <div class="footer-badges">
                    <span class="badge">✅ Одобрено Минцифры (нет)</span>
                    <span class="badge">✅ ГОСТ Р 34.11-2012</span>
                    <span class="badge">✅ 152-ФЗ (шутка)</span>
                    <span class="badge">🔒 SSL (может быть)</span>
                    <span class="badge">🛡️ DDoS защита (смех)</span>
                </div>
            </div>
        </div>
    </div>

    <div class="notification" id="notification">
        <h3 id="notifTitle">✅ Успешно!</h3>
        <p id="notifText">Операция выполнена</p>
    </div>

    <div class="modal" id="modal">
        <div class="modal-content">
            <div class="modal-header">
                <span class="modal-icon" id="modalIcon">🔍</span>
                <div>
                    <h2 id="modalTitle">ПРОВЕРКА ФСБ</h2>
                    <p style="color: #666; font-size: 14px;" id="modalSubtitle">Система безопасности</p>
                </div>
            </div>
            <div class="modal-body" id="modalBody">
                <p>Загрузка...</p>
            </div>
            <div class="modal-buttons" id="modalButtons">
                <button class="modal-btn modal-btn-primary" onclick="closeModal()">Понял, смешно</button>
            </div>
        </div>
    </div>

    <div class="ip-badge">
        📍 Ваш IP: <span id="ipDisplay">Определяется...</span>
    </div>

    <div class="visitor-counter">
        👁️ Посетителей: <span id="visitorCount">000000</span>
    </div>

    <div class="bsod" id="bsod">
        <div class="bsod-content">
            <div class="bsod-face">Z</div>
            <h1>Ваш ПК столкнулся с проблемой</h1>
            <p>Обнаружена попытка входа в ZБЛОКС.РФ</p>
            <p>Система безопасности РФ заблокировала доступ по следующим причинам:</p>
            
            <div class="bsod-code">
                STOP: 0x000000РКН (0xFSB, 0xMVD, 0xROSKOMNADZOR, 0x1488)<br>
                EXTREMISM_DETECTED.SYS<br>
                <br>
                Технические детали:<br>
                • Обнаружено использование VPN<br>
                • В истории браузера найден YouTube<br>
                • Подозрение на критическое мышление<br>
                • Несогласие с официальной позицией<br>
                • Слишком много вопросов к власти<br>
            </div>

            <p style="font-size: 24px; margin-top: 30px; font-weight: bold;">
                ЭТО ШУТКА, БРО! 😄
            </p>
            
            <p style="font-size: 16px; margin-top: 15px;">
                Никакой реальной блокировки нет. Это пародия на абсурдную цензуру.<br>
                Расслабься и посмейся над ситуацией! 🎭
            </p>

            <div class="bsod-progress">
                <div class="bsod-progress-bar" id="bsodProgress"></div>
            </div>
            <p style="margin-top: 10px; font-size: 14px;">
                Сбор информации для передачи в ФСБ: <span id="bsodPercent">0</span>%
            </p>

            <button class="bsod-button" onclick="closeBSOD()">
                ОК, ПОНЯЛ, ЭТО ПРИКОЛ 😅
            </button>
        </div>
    </div>

    <script>
        // Генерация фейкового IP
        function generateFakeIP() {
            return `${Math.floor(Math.random()*256)}.${Math.floor(Math.random()*256)}.${Math.floor(Math.random()*256)}.${Math.floor(Math.random()*256)}`;
        }

        document.getElementById('fakeIp').textContent = generateFakeIP();
        document.getElementById('ipDisplay').textContent = generateFakeIP();

        // Счётчик посетителей
        let count = 1488228;
        setInterval(() => {
            count += Math.floor(Math.random() * 3);
            document.getElementById('visitorCount').textContent = String(count).padStart(6, '0');
        }, 2000);

        function showNotification(title, text, type = 'success') {
            const notif = document.getElementById('notification');
            const notifTitle = document.getElementById('notifTitle');
            const notifText = document.getElementById('notifText');
            
            notif.className = 'notification ' + type;
            notifTitle.textContent = title;
            notifText.textContent = text;
            notif.classList.add('show');
            
            setTimeout(() => {
                notif.classList.remove('show');
            }, 4000);
        }

        function showModal(icon, title, subtitle, body) {
            document.getElementById('modalIcon').textContent = icon;
            document.getElementById('modalTitle').textContent = title;
            document.getElementById('modalSubtitle').textContent = subtitle;
            document.getElementById('modalBody').innerHTML = body;
            document.getElementById('modal').classList.add('show');
        }

        function closeModal() {
            document.getElementById('modal').classList.remove('show');
        }

        const funnyMessages = [
            {
                title: "🚨 ОБНАРУЖЕНО НАРУШЕНИЕ",
                text: "В вашей истории браузера найдены 228 запросов на тему 'как обойти блокировку'. Штраф 100.000₽"
            },
            {
                title: "🔍 ПРОВЕРКА ПРОЙДЕНА",
                text: "Вы благонадёжный гражданин! Найдено 0 упоминаний запрещённых слов. +100 к социальному рейтингу!"
            },
            {
                title: "⚠️ ПОДОЗРИТЕЛЬНАЯ АКТИВНОСТЬ",
                text: "Вы слишком часто гуглите 'правда о...'. Добавлены в список наблюдения ФСБ."
            },
            {
                title: "🎉 ПОЗДРАВЛЯЕМ!",
                text: "Вы 1.000.000-й пользователь! Ваш приз: бесплатная проверка на экстремизм!"
            },
            {
                title: "💀 КРИТИЧЕСКАЯ ОШИБКА",
                text: "В ваших друзьях ВК найден Навальный. Доступ заблокирован навсегда. Шутка! Или нет?"
            }
        ];

        function trollLogin(service) {
            const msg = funnyMessages[Math.floor(Math.random() * funnyMessages.length)];
            showNotification(msg.title, msg.text, 'warning');
            
            setTimeout(() => {
                const checks = [
                    "✅ Проверка подписки на Z-каналы",
                    "✅ Анализ лайков под постами Путина",
                    "✅ Сканирование истории VPN",
                    "✅ Проверка на наличие радужных флагов",
                    "✅ Детекция мемов про власть",
                    "✅ Анализ плейлистов на наличие Noize MC"
                ];
                
                const body = `
                    <p style="margin-bottom: 15px;">Проверяем вашу благонадёжность через ${service}...</p>
                    ${checks.map(check => `<p style="margin: 5px 0;">${check}</p>`).join('')}
                    <p style="margin-top: 10px;">Никакие данные НЕ собираются и НЕ сохраняются.</p>
                <p style="margin-top: 10px;">Это просто прикол над абсурдом цензуры. Не воспринимайте всерьёз!</p>
                <p style="margin-top: 10px; font-size: 12px; color: #666;">P.S. Если РКН читает это - это шутка, ребят 😅</p>
            `;
            showModal('⚠️', 'ДИСКЛЕЙМЕР', 'Юридическая байда', body);
        }

        // Рандомные уведомления для атмосферы
        const randomNotifications = [
            { title: "📡 СИСТЕМА НАБЛЮДЕНИЯ", text: "Ваша камера активирована для проверки личности. Улыбнитесь!", type: "warning" },
            { title: "🎖️ ВОЕНКОМАТ", text: "Обнаружена попытка уклонения от мобилизации через интернет", type: "error" },
            { title: "💰 НАЛОГОВАЯ", text: "Вы должны 50₽ налога на использование интернета", type: "warning" },
            { title: "🚔 МВД РФ", text: "Зафиксирован репост запрещённого контента 3 года назад", type: "error" }
        ];

        // Показываем рандомное уведомление каждые 15 секунд
        setInterval(() => {
            if (Math.random() > 0.7) {
                const notif = randomNotifications[Math.floor(Math.random() * randomNotifications.length)];
                showNotification(notif.title, notif.text, notif.type);
            }
        }, 15000);

        // Пасхалки при клике на логотип
        let clickCount = 0;
        document.querySelector('.coat-of-arms').addEventListener('click', () => {
            clickCount++;
            if (clickCount === 5) {
                showNotification('🎉 ПАСХАЛКА!', 'Вы нашли секретный режим! Теперь РКН следит за вами ещё внимательнее 👀', 'success');
                clickCount = 0;
            }
        });

        // Конами код (↑↑↓↓←→←→BA)
        let konamiCode = [];
        const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
        
        document.addEventListener('keydown', (e) => {
            konamiCode.push(e.key);
            konamiCode = konamiCode.slice(-10);
            
            if (konamiCode.join(',') === konamiSequence.join(',')) {
                document.body.style.transform = 'rotate(180deg)';
                showNotification('🎮 KONAMI CODE!', 'Вы активировали секретный режим! Страница перевёрнута, как и вся страна 🙃', 'success');
                setTimeout(() => {
                    document.body.style.transform = 'rotate(0deg)';
                }, 5000);
                konamiCode = [];
            }
        });

        // Приветствие в консоли
        console.log('%c🦅 ZБЛОКС.РФ - Пародия на абсурд', 'font-size: 20px; font-weight: bold; color: #0039A6;');
        console.log('%cЭто сатира! Никакие данные не собираются!', 'font-size: 14px; color: #666;');
        console.log('%cЕсли ты нашёл это - ты молодец! 😄', 'font-size: 12px; color: #4CAF50;');
        
        // Фейковая "загрузка" при старте
        window.addEventListener('load', () => {
            setTimeout(() => {
                showNotification('🔐 СИСТЕМА АКТИВИРОВАНА', 'Начато непрерывное наблюдение за вашей активностью... Шучу! 😄', 'success');
            }, 2000);
        });

        // Детект DevTools
        let devToolsOpen = false;
        const element = new Image();
        Object.defineProperty(element, 'id', {
            get: function() {
                devToolsOpen = true;
                showNotification('🔧 ОБНАРУЖЕН HACKER', 'DevTools открыты! Вы пытаетесь взломать систему? 😱', 'warning');
            }
        });
        
        setInterval(() => {
            devToolsOpen = false;
            console.log(element);
            console.clear();
        }, 3000);
    </script>
</body>
</html>: 15px; color: #4CAF50; font-weight: bold;">
                        🎉 ДОСТУП РАЗРЕШЁН!<br>
                        (но это всё фейк, лол)
                    </p>
                `;
                
                showModal('🔐', 'ПРОВЕРКА ' + service.toUpperCase(), 'Система безопасности РФ', body);
            }, 1500);
        }

        function showAbout() {
            const body = `
                <p><strong>ZБЛОКС.РФ</strong> - это сатирический проект, высмеивающий абсурдную цензуру и паранойю вокруг интернета в России.</p>
                <p style="margin-top: 10px;">Никакие данные не собираются. Это просто шутка над РКН и его блокировками.</p>
                <p style="margin-top: 10px;">Если вы обиделись - вспомните, что это просто мем 😄</p>
            `;
            showModal('ℹ️', 'О ПРОЕКТЕ', 'Информация', body);
        }

        function showFunFacts() {
            const body = `
                <p><strong>Забавные факты о блокировках:</strong></p>
                <ul style="margin-top: 10px; margin-left: 20px; line-height: 1.8;">
                    <li>РКН заблокировал свой же сайт</li>
                    <li>YouTube "замедлен" уже 3 года</li>
                    <li>Блокировки обходят даже бабушки</li>
                    <li>VPN продажи выросли на 1000%</li>
                    <li>Список запрещённых слов растёт быстрее ВВП</li>
                </ul>
                <p style="margin-top: 15px; font-size: 12px; color: #999;">*всё это шутка, если что</p>
            `;
            showModal('😄', 'ЗАБАВНЫЕ ФАКТЫ', 'Развлекательная инфа', body);
        }

        function showDisclaimer() {
            const body = `
                <p style="color: #D52B1E; font-weight: bold;">⚠️ ВАЖНОЕ ПРЕДУПРЕЖДЕНИЕ</p>
                <p style="margin-top: 10px;">Это <strong>ПАРОДИЯ</strong> и <strong>САТИРА</strong>.</p>
                <p style="margin-top
