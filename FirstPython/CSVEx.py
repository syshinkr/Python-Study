import csv

csv_file = open("C:/Users/admin/Downloads/book_list.csv", 'rt', encoding='UTF8')
csv_reader = csv.reader(csv_file)
book_list = list(csv_reader)

# csv header 제거
book_list = book_list[1:]

# 최초 크롤링 시 있었던 저자 혹은 번역자 데이터의 앞뒤 공백 제거
for item in book_list:
    print(item[1].strip())
    item[1] = item[1].strip()
    item[2] = item[2].strip()

print(book_list)