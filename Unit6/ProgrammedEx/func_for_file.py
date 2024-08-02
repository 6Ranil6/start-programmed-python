# здесь храняться функции для работы с файлами

def creat_file(namefile) :
    outfile = open(f"{namefile}", 'w') 
    outfile.close()