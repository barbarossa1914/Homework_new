from typing import Optional, List, Tuple


class PixelMemory:
    """
    Память Pixel с умным забыванием на основе частоты использования (hit count).
    Хранит не более 10 фактов (вопрос → ответ).
    При переполнении удаляет факт с наименьшим hit_count, при равенстве - самый старый.
    """

    def __init__(self, max_size: int = 10):
        self.max_size = max_size
        # Каждый элемент: (question, answer, hit_count, last_used_index)
        self.memory: List[Tuple[str, str, int, int]] = []
        self.operation_counter = 0
        self.total_answers = 0
        self.correct_answers = 0
        self.verbose = False

    def set_verbose(self, verbose: bool):
        """Включить/выключить подробный вывод"""
        self.verbose = verbose

    def _find_fact_index(self, question: str) -> int:
        """Найти индекс факта по вопросу, если он есть в памяти"""
        for i, (q, _, _, _) in enumerate(self.memory):
            if q == question:
                return i
        return -1

    def _remove_least_important(self):
        """
        Удалить наименее важный факт:
        - Сначала по наименьшему hit_count
        - При равенстве - по самому старому last_used_index
        """
        if not self.memory:
            return

        # Сортируем по (hit_count, last_used_index) и берем первый
        self.memory.sort(key=lambda x: (x[2], x[3]))
        removed = self.memory.pop(0)
        if self.verbose:
            print(f"  [Забыл] '{removed[0]}' (было обращений: {removed[2]})")

    def process(self, line: str) -> Optional[str]:
        """
        Обработать одну строку из потока входящих сообщений.

        Формат строки:
        - "Вопрос → Ответ" - новый факт для запоминания
        - "Вопрос" - запрос к памяти

        Возвращает ответ на вопрос или None, если факт не найден.
        """
        line = line.strip()
        self.operation_counter += 1

        # Проверяем, является ли строка новым фактом (содержит " → ")
        if " → " in line:
            question, answer = line.split(" → ", 1)
            question = question.strip()
            answer = answer.strip()
            self._remember(question, answer)
            return None

        # Иначе это вопрос
        question = line
        answer = self._recall(question)
        return answer

    def _remember(self, question: str, answer: str):
        """Запомнить новый факт"""
        # Проверяем, не знаем ли уже этот вопрос
        idx = self._find_fact_index(question)

        if idx != -1:
            # Обновляем существующий факт
            old_q, _, old_hits, _ = self.memory[idx]
            self.memory[idx] = (question, answer, 0, self.operation_counter)
            if self.verbose:
                print(f"  [Обновил] '{question}' → '{answer}' (было обращений: {old_hits})")
            return

        # Новый факт
        if len(self.memory) < self.max_size:
            self.memory.append((question, answer, 0, self.operation_counter))
            if self.verbose:
                print(f"  [Запомнил] '{question}' → '{answer}' (свободно мест: {self.max_size - len(self.memory)})")
        else:
            if self.verbose:
                print(f"  [Память полна] Нужно запомнить '{question}' → '{answer}'")
            self._remove_least_important()
            self.memory.append((question, answer, 0, self.operation_counter))
            if self.verbose:
                print(f"  [Запомнил] '{question}' → '{answer}'")

    def _recall(self, question: str) -> Optional[str]:
        """Вспомнить ответ на вопрос"""
        idx = self._find_fact_index(question)

        if idx == -1:
            if self.verbose:
                print(f"  [Не знаю] '{question}'")
            return None

        # Нашли факт - увеличиваем hit_count и обновляем last_used
        q, a, hits, _ = self.memory[idx]
        self.memory[idx] = (q, a, hits + 1, self.operation_counter)
        if self.verbose:
            print(f"  [Ответ] '{question}' → '{a}' (обращений: {hits + 1})")

        return a

    def get_memory_contents(self) -> List[Tuple[str, str, int]]:
        """Получить содержимое памяти для отладки (без last_used)"""
        return [(q, a, hits) for q, a, hits, _ in self.memory]

    def verify_answer(self, question: str, expected_answer: str) -> bool:
        """
        Проверить, правильно ли Pixel отвечает на вопрос.
        Используется только для тестирования.
        """
        answer = self._recall(question)
        is_correct = (answer == expected_answer)

        self.total_answers += 1
        if is_correct:
            self.correct_answers += 1

        return is_correct

    def get_accuracy(self) -> float:
        """Получить текущую точность ответов"""
        if self.total_answers == 0:
            return 0.0
        return self.correct_answers / self.total_answers

    def get_memory_size(self) -> int:
        """Получить текущий размер памяти"""
        return len(self.memory)

    def reset_stats(self):
        """Сбросить статистику ответов (для нового теста)"""
        self.total_answers = 0
        self.correct_answers = 0

    def clear_memory(self):
        """Полностью очистить память"""
        self.memory.clear()
        self.operation_counter = 0