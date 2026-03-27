# ⚡ БЫСТРЫЙ СТАРТ - 40 МИНУТ

## Александр, следуйте этим шагам:

### ШАГ 1: Установите Git и Jupyter (если еще нет)
```bash
# Проверьте установку
git --version
jupyter --version

# Если нет - установите:
# Git: https://git-scm.com/download
# Jupyter: pip install jupyter
```

### ШАГ 2: Создайте репозиторий GitHub
1. https://github.com → New repository
2. Название: `ml-iot-lab3`
3. Public
4. Create

### ШАГ 3: Загрузите код
```bash
cd Downloads/lab3-ml-iot
git init
git add .
git commit -m "Lab 3 completed - Davidovich A."
git remote add origin https://github.com/ВАШ_USERNAME/ml-iot-lab3.git
git branch -M main
git push -u origin main
```

### ШАГ 4: Сделайте скриншоты
```bash
# Откройте Git Bash (Windows) или Terminal (Mac/Linux)
cd lab3-ml-iot/data

# Выполните команды и сделайте скриншоты:
awk '{print $1, $2, $5}' list_students.txt
# 📸 Скриншот → сохраните как doc/screenshot_awk.png

sed 's/ЭКТ/КБ/' list_students.txt
# 📸 Скриншот → сохраните как doc/screenshot_sed.png
```

### ШАГ 5: Запустите блокноты
```bash
cd lab3-ml-iot
jupyter notebook
```

**Для каждого файла (task1, task2, task3, task4):**
1. Откройте `.ipynb`
2. Cell → Run All
3. File → Download as → HTML
4. File → Download as → PDF

### ШАГ 6: Загрузите изменения
```bash
git add .
git commit -m "Added exports and screenshots"
git push
```

## ✅ ГОТОВО!

Теперь у вас:
- ✅ Репозиторий на GitHub
- ✅ 4 выполненных задания
- ✅ 8 экспортированных файлов (HTML + PDF)
- ✅ 2 скриншота
- ✅ Отличная оценка!

---

## 📖 Детали

- Полная инструкция: `INSTRUCTION.md`
- Что уже сделано: `THIS_SUMMARY.md`
- Описание проекта: `README.md`

## ⏱️ Время: 40 минут

**Успехов! 🚀**
