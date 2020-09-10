#tadi mama nanyain km.
#aku sayang kamu nda.
#rhx

#TeleBOT + Flask
import telebot
from telebot import types #Tombol
from flask import Flask, request

#Image
from PIL import Image, ImageDraw, ImageFont

#System Command
import os

#Tekss
import random
import json
import textwrap
import re

#Requests
import requests

#Youtube Downloader 
from pytube import YouTube, Playlist

#Command Shell
import subprocess

#TOKEN-API-Telegram
TOKEN = 'API-MU' #MASUKAN-API-TOKENMU-DISINI
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

#Command /start ~ all about kamu.
@bot.message_handler(commands=['start'])
def send_info_start(message):
   text = ('<pre>__________  ___ _______  ___\n\\______   \\/   |   \\   \\/  /\n |       _/    ~    \\     / \n |    |   \\    Y    /     \\ \n |____|_  /\\___|_  /___/\\  \\ \n        \\/       \\/  Bot \\_/\n\n'
      '[#] type <i>/weton</i> menentukan kecocokan jodoh.\n'
      '[#] type <i>/simsimi</i> chat(ting) with chiken.\n'
      '[#] type <i>/youtube</i> download any video or playlist on youtube, with any format output.\n'
      '[#] type <i>/corona</i> get info cases covid-19 in Indo, or spesifik province.\n'
      '[#] type <i>/quote any-text</i> to create image quote.' 
      '\n\n'
      'found bug? tell me <code>t.me/rhxx0</code></pre>')
   bot.send_message(message.chat.id, text, parse_mode='HTML') #Menu

#Command /weton ~ tradisi Jawa sebelum menikah.
@bot.message_handler(commands=['weton'])
def send_info_weton(message):
   bot.send_message(message.chat.id, 'type /end for close.\n\nOiyaa, untuk info lengkap bisa cek disini yaa. <a href="https://mobile.facebook.com/groups/384543601566717?view=permalink&id=3081120845242299&_rdc=1&_rdr">Javanese Society</a>' ,parse_mode='HTML')
   msg = bot.send_message(message.chat.id, 'Siapa namamu?')
   bot.register_next_step_handler(msg, weton_tanya_dua) #Next
   
def weton_tanya_dua(message):
   if message.text == '/end': #End
      bot.send_message(message.chat.id, 'Oke.')
      exit()
   open('aku.txt','w').write(message.text) #Simpan
   msg = bot.send_message(message.chat.id, 'Tanggal lahirmu? (tgl/bln/thn)')
   bot.register_next_step_handler(msg, weton_tanya_tiga) #Next

def weton_tanya_tiga(message):
   if message.text == '/end': #End
      bot.send_message(message.chat.id, 'Oke.')
      exit()
   date = message.text.split('/')
   try: 
      date = date[1]
   except IndexError:
      bot.send_message(message.chat.id, 'Tanggal salah')
   if int(date) > 12 or 0 > int(date) or date.isalpha():
      bot.send_message(message.chat.id, 'Tanggal salah')
   else:
      if int(date[0]) > 32 or 0 > int(date[0]):
         bot.send_message(message.chat.id, 'Tanggal salah')
      else:
         open('aku.txt','a').write('$'+message.text) #Simpan
         msg = bot.send_message(message.chat.id, 'Nama pasanganmu?')
         bot.register_next_step_handler(msg, weton_tanya_empat) #Next

def weton_tanya_empat(message):
   if message.text == '/end':
      bot.send_message(message.chat.id, 'Oke.')
      exit()
   open('aku.txt','a').write('$'+message.text)
   msg = bot.send_message(message.chat.id, 'Tanggal lahir pasanganmu? (tgl/bln/thn)')
   bot.register_next_step_handler(msg, weton_eksekusi) #Next

def hitung_weton(z,v): #Menghitung hari dan pasaran
   l = v.split('/')
   if int(l[2])%4 == 0:
      a = ['',31,29,31,30,31,30,31,31,30,31,30,31]
   else:
      a = ['',31,28,31,30,31,30,31,31,30,31,30,31]
   o = int(l[0])
   w = int(l[1])
   q = sum(a[1:w])
   b = q+o
   c = int((int(l[2])-1)/4)
   d = (int(l[2])+b+c)%7
   e = (c+b)%5
   return d,e,z,v

def weton_eksekusi(message):
   if message.text == '/end': #End
      bot.send_message(message.chat.id, 'Oke.')
      exit()
   date = message.text.split('/')
   try:
      date = date[1]
   except IndexError:
      bot.send_message(message.chat.id, 'Tanggal salah')
   if int(date) > 12 or 0 > int(date):
      bot.send_message(message.chat.id, 'Tanggal salah')
   else:
      if int(date[0]) > 32 or 0 > int(date[0]):
         bot.send_message(message.chat.id, 'Tanggal salah')
      else:
         open('aku.txt','a').write('$'+message.text)
   entot = open('aku.txt','r').readlines() #Buka Jawaban
   x = entot[0].split('$')
   rohman = hitung_weton(x[0],x[1]) #Method rohman
   nanda = hitung_weton(x[2],x[3]) #Method nanda
   day = ["Jum'at","Sabtu","Minggu","Senin","Selasa","Rabu","Kamis"] #Hari list
   pasaran = ["Legi","Pahing","Pon","Wage","Kliwon"] #Pasaran list
   ankday = [6,9,5,4,3,7,8] #Hitungan hari
   ankpasaran = [5,9,7,4,8] #Hitugan pasaran
   k = (ankday[rohman[0]]+ankpasaran[rohman[1]])+(ankday[nanda[0]]+ankpasaran[nanda[1]]) #Hitung weton
   text = (
   'Nama kamu : ' + rohman[2] + '\n'
   'Tgl lahir : ' + rohman[3] + '\n'
   'Pasaran : ' + day[rohman[0]] + ' ' + pasaran[rohman[1]] + '\n'
   'Jumlah : ' + str(ankday[rohman[0]]) + '+' + str(ankpasaran[rohman[1]]) + '=' + str(ankday[rohman[0]]+ankpasaran[rohman[1]]) + '\n\n'
   'Pasanganmu : '+ nanda[2] + '\n'
   'Tgl lahir : '+ nanda[3] + '\n'
   'Pasaran : '+ day[nanda[0]] + ' ' + pasaran[nanda[1]] + '\n'
   'Jumlah : '+ str(ankday[nanda[0]]) + '+' + str(ankpasaran[nanda[1]]) + '=' + str(ankday[nanda[0]]+ankpasaran[nanda[1]]) + '\n\n'
   'Angka weton : '+ str(k)
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML')
   #Semua weton list
   pegat = [1,9,10,18,19,27,28,36,'Pegat','"Hasil pegat, bahwa menurut hitungan weton jawa kemungkinan pasangan akan sering mendapatkan masalah di kemudian hari, bisa saja masalah ekonomi, kekuasaan, perselingkuhan hingga menyebabkan pasangan bercerai."']
   ratu = [2,11,20,29,'Ratu','"Hasil Ratu, menurut hitungan weton jawa bisa dikatakan bahwa pasangan ini memang sudah jodohnya. Karena didalam kehidupan nanti keluarganya akan sangat dihargai dan disegani oleh tetangga maupun masyarakat sekitar. Bahkan banyak orang yang iri hati karena keharmonisannya dalam membina rumah tangga."']
   jodo = [3,12,21,30,'Jodoh','"Hasil Jodoh, menurut hitungan weton jawa pasangan ini memang beneran cocok dan berjodoh. Karena dapat saling menerima baik kelebihan atau kekurangannya. Selain itu rumah tangganya dapat rukun sampai tua nanti."']
   topo = [4,13,22,31,'Topo','"Hasil Topo, menurut hitungan jawa di gambarkan dalam membina rumah tangga nanti akan mengalami kesusahan di awal, tetapi akan bahagia di akhir nanti. Masalah ini bisa saja karena masalah ekonomi dan masih banyak lagi. Namun ketika sudah mempunyai anak dan cukup lama berumah tangga, di hari itulah kehidupanya akan menjadi sukses dan bahagia."']
   tinari = [5, 14, 23, 32,'Tinari','"Hasil Tinari, menurut hitungan weton jawanya berarti akan menemukan kebehagaiaan dimasa nanti. Selain itu gampang dalam mencari rezeki dan sering mendapatkan keberuntungan."']
   padu = [6, 15, 24, 33,'Padu','"Hasil Padu, menurut hitungan weton jawa digambarkan dalam berumah tangganya nanti akan sering mengalami sebuah pertengkaran. Namun tidak sampai mengarah ke seuah perceraian. Masalah pertengkaran ini digambarkan hanya masalah yang sifatnya cukup sepele."']
   sujanan = [7, 16, 25, 34,'Sujanan','"Hasil sujanan, menurut hitungan weton jawa digambarkan bahwa dalam berumah tangganya nanti akan mengalami sebuah pertengkaran, bisa saja kerana perselingkuhan yang terjadi yang di mulai dari pahak laki-laki atau si perempuan."']
   pesthi = [8, 17, 26, 35,'Pesthi','"Hasil Pesthi, menurut hitungan weton jawa digambarkan bahwa dalam berumah tangganya nanti akan selalu rukun, tenteram, adem ayem hingga tua nanti. Meskipun ada masalah, namun tidak akan bisa merusak keharmonisan keluarganya."']
   if k in pegat:
      weton = '' + pegat[8] + '\n' + pegat[9]
      bot.send_message(message.chat.id, weton, parse_mode='HTML')
   elif k in ratu:
      weton = '' + ratu[4] + '\n' + ratu[5]
      bot.send_message(message.chat.id, weton, parse_mode='HTML')
   elif k in jodo:
      weton = '' + jodo[4] + '\n' + jodo[5]
      bot.send_message(message.chat.id, weton, parse_mode='HTML')
   elif k in topo:
      weton = '' + topo[4] + '\n' + topo[5]
      bot.send_message(message.chat.id, weton, parse_mode='HTML')
   elif k in tinari:
      weton = '' + tinari[4] + '\n' + tinari[5]
      bot.send_message(message.chat.id, weton, parse_mode='HTML')
   elif k in padu:
      weton = '' + padu[4] + '\n' + padu[5]
      bot.send_message(message.chat.id, weton, parse_mode='HTML')
   elif k in sujanan:
      weton = '' + sujanan[4] + '\n' + sujanan[5]
      bot.send_message(message.chat.id, weton, parse_mode='HTML')
   elif k in pesthi:
      weton = '' + pesthi[4] + '\n' + pesthi[5]
      bot.send_message(message.chat.id, weton, parse_mode='HTML')

#Command /corona ~ kasus di Indonesia
@bot.message_handler(commands=['corona'])
def send_info_corona(message):
   txt = message.text.replace('/corona ','',1)
   txt = str(txt)
   if txt == '/corona':
      r = requests.get('https://indonesia-covid-19.mathdro.id/api') #API kasus Covid-19 di Indonesia by. mathdroid
      data = r.json()
      text = (
         "<b>Indonesia Kasus Covid-19\n\n"
         "Total Kasus : "+str(data['jumlahKasus'])+"\n"
         "Sembuh : "+str(data['sembuh'])+"\n"
         "Positif/dirawat : "+str(data['perawatan'])+"\n"
         "Meninggal : "+str(data['meninggal'])+"\n\n"
         "Bisa menampilkan data lebih spesifik berdasarkan provinsi. ex: <pre>/corona yogya</pre></b>"
         )
   else:
      r = requests.get('https://data.covid19.go.id/public/api/prov.json') #API kasus Covid-19 berdasarkan Provinsi by Pemerintah Indonesia
      dataa = r.json()
      for x in range(0,33):
         if txt.upper() in dataa['list_data'][x]['key']:
            text = (
            "<b>" + str(dataa['list_data'][x]['key']) + "\n"
            "Last update : " + str(dataa['last_date']) + "\n\n"
            "Jumlah kasus : " + str(dataa['list_data'][x]['jumlah_kasus']) + "\n\n"
            "Dirawat : " + str(dataa['list_data'][x]['jumlah_dirawat']) + ' (+' + str(dataa['list_data'][x]['penambahan']['positif']) + ")\n"
            "Sembuh : " + str(dataa['list_data'][x]['jumlah_sembuh']) + ' (+' + str(dataa['list_data'][x]['penambahan']['sembuh']) + ")\n"
            "Meninggal : " + str(dataa['list_data'][x]['jumlah_meninggal']) + ' (+' + str(dataa['list_data'][x]['penambahan']['meninggal'])+')</b>'
            )
   bot.send_message(message.chat.id, text, parse_mode="HTML")

#Command /simsimi
@bot.message_handler(commands=['simsimi'])
def send_info_simsimi(message):
   simsimi_logo = ('<pre> _____ _           _       _ \n'
  '|   __|_|_____ ___|_|_____|_|\n'
  '|__   | |     |_ -| |     | |_ \n'
  '|_____|_|_|_|_|___|_|_|_|_|_|_|</pre>\n---------\ntype /end to end.')
   msg = bot.send_message(message.chat.id, simsimi_logo, parse_mode='HTML')
   bot.register_next_step_handler(msg, main_simsimi)

def main_simsimi(message):
   if message.text == '/end':
      bot.send_message(message.chat.id, 'trims.')
      exit()
   headers = {
      'Content-Type': 'application/json',
      'x-api-key': 'APP-KEY MU', #Simsimi API-Key (daftar akun trial/bayar sewa API)
   }
   data = '{\n            "utext": "'+message.text+'", \n            "lang": "id" \n     }'
   response = requests.post('https://wsapi.simsimi.com/190410/talk', headers=headers   , data=data)
   ass = response.json()
   if ass['status'] == 200:
      msg = bot.send_message(message.chat.id, ass['atext'], parse_mode="HTML")
      bot.register_next_step_handler(msg, main_simsimi)
   else:
      bot.send_message(message.chat.id, 'maaf simsimi sedang bobok. error',ass['statusMessage'],  
   parse_mode="HTML")

#Command /youtube ~ Youtube mp3 / video downloader
@bot.message_handler(commands=['youtube'])
def send_info_youtube(message):
   text = ('<pre>        __      __                \n .--.--|  |_.--|  .--.--.--.-----.\n |  |  |   _|  _  |  |  |  |     |\n |___  |____|_____|________|__|__|\n |_____|[by. rhxx anjay gurinjay]</pre>')
   bot.send_message(message.chat.id, text, parse_mode="HTML")
   msg = bot.send_message(message.chat.id, 'Pastekan url playlist/video disini, atau bisa cari dengan <code>@vid title</code>.', parse_mode="HTML")
   bot.register_next_step_handler(msg, youtube_dl)

def youtube_dl(message):
   if 'playlist' in message.text:
      play = Playlist(message.text)
      play._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
      k = str(play.video_urls)
      open('rohman.txt','w').write(k)
      #Tombol
      markup = types.InlineKeyboardMarkup()
      markup.row(
         types.InlineKeyboardButton(text="video/mp4 360p", callback_data="playlist_360"),
         types.InlineKeyboardButton(text="video/mp4 720p", callback_data="playlist_720"))
      markup.row(types.InlineKeyboardButton(text='audio/mp3', callback_data="playlist_mp3"))
      bot.send_message(message.chat.id, '.',reply_markup=markup) 
   else:
      open('nanda.txt','w').write(message.text)
      #Tombol
      markup = types.InlineKeyboardMarkup()
      markup.row(
         types.InlineKeyboardButton(text="video/mp4 360p", callback_data="360"),
         types.InlineKeyboardButton(text="video/mp4 720p", callback_data="720"))
      markup.row(types.InlineKeyboardButton(text='audio/mp3', callback_data="mp3"))
      bot.send_message(message.chat.id, 'Silahkan dipilih.', reply_markup=markup) 

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
   bot.answer_callback_query(callback_query_id=call.id, text='Tunggu ya sayang!')
   #Single video
   if call.data == '360':
      entot = open('nanda.txt','r').readlines()
      ytku = YouTube(str(entot))
      try:
         ytku.streams.get_by_itag(18).download()
         name = str(ytku.title).replace('.','').replace('|','')+'.mp4'
         video = open(name, 'rb')
         bot.send_video(call.message.chat.id, video)
         os.remove(name)
      except AttributeError:
         bot.send_message(call.message.chat.id, 'Maaf 360p tidak tersedia.', parse_mode="HTML")
   if call.data == '720':
      entot = open('nanda.txt','r').readlines()
      ytku = YouTube(str(entot))
      try:
         ytku.streams.get_by_itag(22).download()
         name = str(ytku.title).replace('.','').replace('|','')+'.mp4'
         video = open(name, 'rb')
         bot.send_video(call.message.chat.id, video)
         os.remove(name)
      except AttributeError:
         bot.send_message(call.message.chat.id, 'Maaf 720p tidak tersedia.', parse_mode="HTML")
   if call.data == 'mp3':
      entot = open('nanda.txt','r').readlines()
      ytku = YouTube(str(entot))
      try:
         ytku.streams.get_by_itag(18).download()
         name = str(ytku.title).replace('.','').replace('|','')+'.mp4'
         name2 = str(ytku.title)+'.mp3'
         cmd = ['ffmpeg', '-i', name, '-vn', '-f','mp3',name2]
         subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
         audio = open(name2, 'rb')
         bot.send_audio(call.message.chat.id, audio)
      except AttributeError:
         bot.send_message(call.message.chat.id, 'Maaf versi audio/mp3 tidak tersedia.', parse_mode="HTML")
   #Handler tombol playlist
   if call.data == 'playlist_360':
      entot = open('rohman.txt','r').readlines()
      k = entot[0]
      k = k.replace('[','').replace(']','')
      k = k.split(',')
      for url in k:
         try:
            ytku = YouTube(url)
            bot.send_message(call.message.chat.id, ytku.title)
            ytku.streams.get_by_itag(18).download()
            name = str(ytku.title).replace('.','').replace('|','')+'.mp4'
            video = open(name, 'rb')
            bot.send_video(call.message.chat.id, video)
            os.remove(name)
         except AttributeError:
            bot.send_message(call.message.chat.id, 'Maaf 360p tidak tersedia.', parse_mode="HTML")
         except:
            pass
   if call.data == 'playlist_720':
      entot = open('rohman.txt','r').readlines()
      k = entot[0]
      k = k.replace('[','').replace(']','')
      k = k.split(',')
      for url in k:
         try:
            ytku = YouTube(url)
            bot.send_message(call.message.chat.id, ytku.title)
            ytku.streams.get_by_itag(22).download()
            name = str(ytku.title).replace('.','').replace('|','')+'.mp4'
            video = open(name, 'rb')
            bot.send_video(call.message.chat.id, video)
            os.remove(name)
         except AttributeError:
            bot.send_message(call.message.chat.id, 'Maaf 720p tidak tersedia.', parse_mode="HTML")
         except:
            pass
   if call.data == 'playlist_mp3':
      entot = open('rohman.txt','r').readlines()
      k = entot[0]
      k = k.replace('[','').replace(']','')
      k = k.split(',')
      for url in k:
         try:
            ytku = YouTube(url)
            ytku.streams.get_by_itag(18).download()
            name = str(ytku.title).replace('.','').replace('|','')+'.mp4'
            name2 = str(ytku.title)+'.mp3'
            cmd = ['ffmpeg', '-i', name, '-vn', '-f','mp3',name2]
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            audio = open(name2, 'rb')
            bot.send_audio(call.message.chat.id, audio)
         except AttributeError:
            bot.send_message(call.message.chat.id, 'Maaf versi audio/mp3 tidak tersedia.', parse_mode="HTML")
         except:
            pass

#Command /quote ~ asikk
@bot.message_handler(commands=['quote'])
def send_info_quote(message):
   quotetxt = message.text.replace('/quote ', '',1)
   xx = textwrap.wrap(quotetxt, width=40)
   MAX_W = 640
   background = Image.open(requests.get('https://source.unsplash.com/640x640/?japan,korea', stream=True).raw).convert('RGBA') # get image
   overlaw = Image.open("assets/overlaw.png").convert('RGBA')
   fto = Image.blend(overlaw, background, 0.5)
   draw = ImageDraw.Draw(fto)
   font = ImageFont.truetype('assets/font.ttf', 28)
   atas, paf = 280, 10
   for i in xx:
      w, h = draw.textsize(i, font=font)
      draw.text(((MAX_W - w) / 2, atas), i, font=font)
      atas += h + paf
   fto.save('assets/a.PNG')
   bot.send_photo(message.chat.id, photo=open('assets/a.PNG', 'rb'))

#Kirim Pesan
def sendMessage(message, text):
   bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda msg: msg.text is not None)
def reply_to_message(message):
   sendMessage(message, 'hai {}, cek fitur disini /start'.format(message.from_user.first_name))

#Server Webhook
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "sukses!", 200
@server.route("/")
def webhook():
   appname = 'Heroku APP Mu' #Nama app Heroku
   bot.remove_webhook()
   bot.set_webhook(url='https://'+appname+'.herokuapp.com/' + TOKEN) 
   return "sukses!", 200
if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

#Terimakasi buat semua yang terlibat disini.