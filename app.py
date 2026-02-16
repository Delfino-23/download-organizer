"""
Download Organizer - organiza automaticamente sua pasta de Downloads
Roda em background e move arquivos pras pastas certas
"""

import os
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DownloadOrganizer(FileSystemEventHandler):
    def __init__(self, downloads_path):
        self.downloads_path = Path(downloads_path)

        # Define categosrias
        self.categories = {
            'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
            'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
            'Musicas': ['.mp3', '.wav', '.flac'],
            'Compactados': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'Executaveis': ['.exe', '.msi', '.deb', '.dmg'],
            'Codigo': ['.py', '.js', '.html', '.css', '.java', '.cpp']
        }

        # Cria pastas se não existirem
        for category in self.categories.keys():
            (self.downloads_path / category).mkdir(exist_ok=True)
    
    def on_created(self, event):
        """Quando um arquivo novo é criado"""
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)

        # Espera o arquivo terminar de baixar
        time.sleep(1)

        # Organiza
        self.organize_file(file_path)
    
    def organize_file(self, file_path):
        """Move o arquivo pra pasta certa"""
        if not file_path.exists():
            return
        
        extension = file_path.suffix.lower()

        # Encontra categoria
        for category, extensions in self.categories.items():
            if extension in extensions:
                dest = self.downloads_path / category / file_path.name

                # Evita sobrescrever
                if dest.exists():
                    name = file_path.stem
                    dest = self.downloads_path / category / f"{name}_1{extension}"

                file_path.rename(dest)
                print(f'Movido: {file_path} -> {dest}/')
                return
        # Se não encontrou categoria, deixa na pasta de Downloads
        print(f'Arquivo sem categoria: {file_path}')
    
    def organize_existing(self):
        """Organiza arquivos que já estão na pasta"""
        print("Organizando arquivos existentes...\n")

        files = [f for f in self.downloads_path.iterdir()
                 if f.is_file() and not f.name.startswith('.')]
        
        for file_path in files:
            self.organize_file(file_path)
        
        print(f"\n{len(files)} arquivo(s) organizado(s)!")

def main():
    # Path do Downloads no Windos via WSL
    downloads = Path.home() / 'Downloads'

    organizer = DownloadOrganizer(downloads)

    # Organiza arquivos existentes
    organizer.organize_existing()

    # Monitora novos arquivos
    print(f"\n Monitorando: {downloads}")
    print("(Pressione Ctrl+C para parar)\n")

    observer = Observer()
    observer.schedule(organizer, str(downloads), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n\n Organizer encerrado")
    
    observer.join()

if __name__ == "__main__":
    main()