# rhxBOT - Telegram Bot 
Sebuah Telegram Bot yang saya buat karena gabut menggunakan kode program python3, ada beberapa fitur diantaranya.
  - Youtube Downloader (download video/mp3)
  - Kecocokan (menghitung kecocokan weton)
  - Quote Maker (Membuat image quote)
  - Kasus Corona info di Indonesia

demo : [t.me/rhxx_bot](https://t.me/rhxx_bot)




### Cara Install

Saya menggunakan server Heroku, jadi sebelum itu pastikan saudara sudah membuat App di Heroku. Karena ini sebuah bot Telegram maka dibutuhkan sebua API dari telegram saudara bisa mendapatkannya dari [@BotFather](https://t.me/BotFather).

```sh
$ git clone https://github.com/rohmnnn/rhxbot.git
$ cd rhxbot
```

Edit file **bot.py** tambahkan API Telegram, APP-Key Simsimi dan Nama APP Heroku mu.
Install  [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), sudah didalam folder rhxbot lanjut perintah.
```sh
$ heroku login
$ heroku buildpacks:add https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git
$ git init
$ heroku git:remote -a namaappheroku
$ git add *
$ git commit -am 'some teks'
$ git push heroku master
```

--------------------------------
PytelegramBotAPI, pytube3, Simsimi, Flask, Heroku, Pemerintah Indonesia, JejakaTuorial, Unplash, stackoverflow, Python3, mathdroid dan semua yang terlibat. <3 

