from googleapiclient.discovery import build

def get_video_info(api_key, video_id):
    # Инициализируем объект YouTube Data API с помощью ключа разработчика
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Создаем запрос к API YouTube для получения информации о видео по его ID
    request = youtube.videos().list(
        part='snippet',  # Указываем, что нас интересует только информация о видео (название, описание и т.д.)
        id=video_id  # Указываем ID видео, из которого нужно получить информацию
    )

    # Выполняем запрос и получаем ответ
    response = request.execute()

    # Извлекаем заголовок и описание видео из ответа
    title = response['items'][0]['snippet']['title']
    description = response['items'][0]['snippet']['description']

    # Возвращаем заголовок и описание видео
    return title, description

# Ваш API ключ YouTube Developer и ID видео, из которого нужно получить информацию
api_key =
video_id = 'IpBhhbA1Hds'

# Получаем заголовок и описание видео
video_title, video_description = get_video_info(api_key, video_id)

# Выводим заголовок и описание видео
print("Заголовок видео:", video_title)
print("Описание видео:", video_description)
