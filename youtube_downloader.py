from pytube import YouTube
import os

class youtubeDownloader():
	def __init__(self):
		pass

	def downloader(self):
		while True:
			os.system('cls')
			self.user_input = input("İndirme işlemi yapmak istiyormusunuz?\n(y/n): ")
			
			if self.user_input == "y":
				self.choose_p = input("Lütfen wav-mp4 seçimini yapınız (mp3/mp4): ")
				
				if self.choose_p == "mp3":
					os.system('cls')
					self.youtube_link = input("Lütfen indirmek istediğiniz youtube linkini giriniz: ")
					self.yt_download = YouTube(self.youtube_link)
					print(f"{self.yt_download.title}, mp3 formatında yükleniyor...")
					self.stream = self.yt_download.streams.get_by_itag(251)
					self.stream.download("C:/Users/murat/Music/")
					#os.rename(rf"/home/murat/Music/{self.yt_download.title}.webm", rf"/home/murat/Music/{self.yt_download.title}.mp3")

					self.change_file_name = input("Dosya ismini değiştirmek istermisiniz?\n(y/n): ")
					if self.change_file_name == "y":
						new_file = input("Lütfen yeni dosya ismini giriniz: ")
						old_name = rf"C:/Users/murat/Music/{self.yt_download.title}.webm"
						new_name = rf"C:/Users/murat/Music/{new_file}.mp3"
						os.rename(old_name, new_name)
					else:
						continue
					
					print("Yükleme işlemi tamamlandı...")

				elif self.choose_p == "mp4":
					os.system('cls')
					self.youtube_link = input("Lütfen indirmek istediğiniz youtube linkini giriniz: ")
					self.yt_download = YouTube(self.youtube_link)
					print(f"{self.yt_download.title}, mp4 formatında yükleniyor...")
					self.stream = self.yt_download.streams.get_highest_resolution()
					self.stream.download("C:/Users/murat/Music/")
					self.change_file_name = input("Dosya ismini değiştirmek istermisiniz?\n(y/n): ")
					if self.change_file_name == "y":
						new_file = input("Lütfen yeni dosya ismini giriniz: ")
						old_name = rf"C:/Users/murat/Music/{self.yt_download.title}.mp4"
						new_name = rf"C:/Users/murat/Music/{new_file}.mp4"
						os.rename(old_name, new_name)
					else:
						continue
					
					print("Yükleme işlemi tamamlandı...")
			
			elif self.user_input == "n":
				print("İyi günler!")
				exit()

my_instance = youtubeDownloader()
my_instance.downloader()