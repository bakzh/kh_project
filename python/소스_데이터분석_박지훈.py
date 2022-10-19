file = 'd:\\javaedu9\\project\\python\\exam.txt'
stop = False
dictionary = {}
try :
   f = open(file, 'w',encoding='UTF8')
except FileNotFoundError as e :
    pass
else :
    open(file, 'a',encoding='UTF8')
    if f.readable() :
        for line in f.readlines() :
            list = line.split(':')
            dictionary[list[0].strip()] = list[1].strip()
            f.close()

while not stop :

        menu = input('<영어 단어장> 메뉴] 1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료(x) : ')
        if(menu == '1') :
            if(len(dictionary) > 4) :
                print('최대 5단어만 저장할 수 있습니다')
                continue
            else :
                en_saveWord = input('영어 단어를 입력하세요 : ')
                ko_saveWord = input('뜻을 입력하세요 : ')
                dictionary[en_saveWord] = ko_saveWord

        if(menu == '2') :
            en_searchWord = input('검색할 단어를 입력하세요 : ').lower()
            notFound = dictionary.get(en_searchWord)
            if (notFound == None) :
                    print('단어를 검색할 수 없습니다')
            for key in dictionary.keys() :
                if(key == en_searchWord) :
                    print('{} : {}'.format(en_searchWord,dictionary.get(en_searchWord)))


        if(menu == '3') :
            en_updateWord = input('수정할 단어를 입력하세요 : ').lower()
            notFound = dictionary.get(en_updateWord)
            if (notFound == None) :
                print('단어를 검색할 수 없습니다')
            for key in dictionary.keys() :
                if(key == en_updateWord) :
                    ko_updateWord = input('뜻을 입력하세요 : ')
                    dictionary[en_updateWord] = ko_updateWord
                    print('단어의 뜻을 수정하였습니다')
        
        if(menu == '4') :
            en_deleteWord = input('삭제할 단어를 입력하세요 : ').lower()
            notFound = dictionary.get(en_deleteWord)
            if (notFound == None) :
                print('단어를 검색할 수 없습니다')
            for key in list(dictionary.keys()) :
                if(key == en_deleteWord) :
                    del dictionary[en_deleteWord]
                    print('단어를 삭제하였습니다')

        if(menu == '5') :
            sub_menu = input('1.오름차순 2.내림차순 : ')
            import operator
            sort = sorted(dictionary.items(),key=operator.itemgetter(0))
            reverseSort = reversed(sort)
            print(sort)
            if(sub_menu == '1') :
                for item in sort :
                    print('{} : {}'.format(item[0],item[1]))
                continue
            elif(sub_menu == '2') :
                for item in reverseSort :
                    print('{} : {}'.format(item[0],item[1]))
                continue
            else :
                print('잘못 입력하셨습니다')
        
        if(menu == '6') :
            savedWord = len(dictionary)
            print('1.저장된 단어 갯수 : {}'.format(savedWord))
            longWordLength = None 
            for items in dictionary.keys() :
                longWordLength = items
                for item in dictionary.keys() :
                    if len(longWordLength) <= len(item) :
                        longWordLength = item
            print('2.단어의 문자수가 가장 많은 단어 : {}'.format(longWordLength))
            print('3.단어 글자수 내림차순 : ')

        if(menu == 'x' or menu == 'X') :
            f = open(file, 'w',encoding='UTF8')
            if f.writable() :
                for item in dictionary.items() :
                    f.write('{}:{}\n'.format(item[0].strip(),item[1].strip()))
                f.close()
            stop = True
            continue
