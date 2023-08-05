from aiogram.dispatcher.filters.state import State, StatesGroup


class FileState(StatesGroup):
    file = State()


class FileStateWord(StatesGroup):
    file = State()


class ImageTotext(StatesGroup):
    image = State()

class ImageTopdf(StatesGroup):
    image = State()