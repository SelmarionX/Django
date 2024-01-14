from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def home(request):
    logger.info("Посещение главной страницы")
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Это моя первая страница на Django.</p>
    """
    return HttpResponse(html)


def about(request):
    logger.info("Посещение страницы 'Обо мне'")
    html = """
    <h1>Обо мне</h1>
    <p>Меня зовут Иван Иванов. Я начинающий разработчик Django.</p>
    """
    return HttpResponse(html)
