"""
Convertendo vídeos com FFMPEG

Obs: Este arquivo foi executado somente em ambiente Linux

Sintaxe: 

ffmpeg -i "ENTRADA" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k -c:s srt -map v:0 -map a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAIDA"
"""

import os
import fnmatch
import sys

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'<insira o caminho do executável>'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

if __name__ == '__main__':
    print('Aula - Convertendo arquivos com FFMPEG')
    print()

    caminho_origem = '/mnt/d/Movies'
    caminho_destino = '/mnt/d/Movies/saida'

    print('Arquivos encontrados no diretório', caminho_origem)
    for raiz, pastas, arquivos in os.walk(caminho_origem):
        for arquivo in arquivos:
            if fnmatch.fnmatch(arquivo, '*.mp4'):
                print('-', arquivo)
                caminho_completo = os.path.join(raiz, arquivo)
                #print(caminho_completo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                arquivo_legenda = os.path.join(raiz, nome_arquivo + '.srt')
                #print(arquivo_legenda)
                if os.path.isfile(arquivo_legenda):
                    #print('Legenda existe!')
                    input_legenda = f'-i "{arquivo_legenda}"'
                    map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
                else:
                    #print('Legenda não existe!')
                    input_legenda = ''
                    map_legenda = ''

                arquivo_saida = f'{caminho_destino}/{nome_arquivo}_novo{extensao_arquivo}'

                comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                    f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
                    f'{debug} {map_legenda} {arquivo_saida}'
                print()
                os.system(comando)
                print()

            
            



