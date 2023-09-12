from aiogram.dispatcher.filters.state import State, StatesGroup


class FileState(StatesGroup):
    file = State()


class FileStateWord(StatesGroup):
    file = State()


class ImageTotext(StatesGroup):
    image = State()

class ImageTopdf(StatesGroup):
    image = State()


class ImageToGet_text(StatesGroup):
    file = State()

class Excel_to_pdf_state(StatesGroup):
    file = State()