# Функция возвращает количество строк и содержимое файла
def get_file_data(filename):
  with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
  return len(lines), lines


# Запись данных из файлов 1.txt - 2.txt в файл result.txt
def write_to_result(file_list, output_file):
  with open(output_file, 'w', encoding='utf-8') as result:
    for filename, (line_count, content) in file_list:
      result.write(f"{filename}\n")
      result.write(f"{line_count}\n")
      result.writelines(content)
      result.write("\n")


# Список файлов для обработки
def main():
  files = ['1.txt', '2.txt', '3.txt']
  file_data = []

  # Получаем информацию о каждом файле
  for filename in files:
    line_count, content = get_file_data(filename)
    file_data.append((filename, (line_count, content)))

  # Сортировка файлов по количеству строк
  file_data.sort(key=lambda x: x[1][0])

  # Запись отсортированного содержимого файлов в result.txt
  write_to_result(file_data, 'result.txt')
if __name__ == "__main__":
  main()


# Вывод на печать содержания файла result.txt
print(f' \n')
with open('result.txt', 'r', encoding='utf-8') as f:
  for line in f:
    print(line.strip())

print(f' \n')