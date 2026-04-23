import random
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from threading import Thread
import time
from typing import List, Tuple, Dict, Optional
from collections import defaultdict
from pixel_memory import PixelMemory


class PixelTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pixel Memory Test - Система тестирования")
        self.root.geometry("900x750")

        # Переменные для теста
        self.test_running = False
        self.pixel = None
        self.test_thread = None

        self.setup_ui()

    def setup_ui(self):
        # Основной контейнер
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Настройка весов
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)

        # Заголовок
        title_label = ttk.Label(main_frame, text="Тестирование памяти Pixel",
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, pady=10)

        # Панель настроек
        settings_frame = ttk.LabelFrame(main_frame, text="Настройки теста", padding="10")
        settings_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)
        settings_frame.columnconfigure(1, weight=1)

        # Количество уникальных вопросов
        ttk.Label(settings_frame, text="Количество уникальных вопросов (база):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.unique_questions_var = tk.IntVar(value=20)
        unique_spinbox = ttk.Spinbox(settings_frame, from_=5, to=50, textvariable=self.unique_questions_var, width=10)
        unique_spinbox.grid(row=0, column=1, sticky=tk.W, pady=5, padx=10)
        ttk.Label(settings_frame, text="(первые 30% станут 'важными')").grid(row=0, column=2, sticky=tk.W, pady=5)

        # Количество операций
        ttk.Label(settings_frame, text="Количество операций:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.total_ops_var = tk.IntVar(value=200)
        ops_spinbox = ttk.Spinbox(settings_frame, from_=20, to=500, textvariable=self.total_ops_var, width=10)
        ops_spinbox.grid(row=1, column=1, sticky=tk.W, pady=5, padx=10)
        ttk.Label(settings_frame, text="(включая запоминание и вопросы)").grid(row=1, column=2, sticky=tk.W, pady=5)

        # Вероятность важного вопроса
        ttk.Label(settings_frame, text="Вероятность важного вопроса:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.importance_var = tk.DoubleVar(value=0.7)
        importance_scale = ttk.Scale(settings_frame, from_=0.0, to=1.0, variable=self.importance_var, orient=tk.HORIZONTAL)
        importance_scale.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=10)
        self.importance_label = ttk.Label(settings_frame, text="70%")
        self.importance_label.grid(row=2, column=2, sticky=tk.W, pady=5)

        def update_importance_label(*args):
            self.importance_label.config(text=f"{self.importance_var.get():.0%}")
        self.importance_var.trace('w', update_importance_label)

        # Размер памяти
        ttk.Label(settings_frame, text="Размер памяти Pixel:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.memory_size_var = tk.IntVar(value=10)
        memory_spinbox = ttk.Spinbox(settings_frame, from_=5, to=20, textvariable=self.memory_size_var, width=10)
        memory_spinbox.grid(row=3, column=1, sticky=tk.W, pady=5, padx=10)
        ttk.Label(settings_frame, text="(максимум фактов)").grid(row=3, column=2, sticky=tk.W, pady=5)

        # Вероятность нового факта
        ttk.Label(settings_frame, text="Вероятность нового факта:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.new_fact_prob_var = tk.DoubleVar(value=0.3)
        new_fact_scale = ttk.Scale(settings_frame, from_=0.0, to=0.8, variable=self.new_fact_prob_var, orient=tk.HORIZONTAL)
        new_fact_scale.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=10)
        self.new_fact_label = ttk.Label(settings_frame, text="30%")
        self.new_fact_label.grid(row=4, column=2, sticky=tk.W, pady=5)

        def update_new_fact_label(*args):
            self.new_fact_label.config(text=f"{self.new_fact_prob_var.get():.0%}")
        self.new_fact_prob_var.trace('w', update_new_fact_label)

        # Кнопки управления
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, pady=10)

        self.start_button = ttk.Button(control_frame, text="Начать тест", command=self.start_test)
        self.start_button.grid(row=0, column=0, padx=5)

        self.stop_button = ttk.Button(control_frame, text="Остановить", command=self.stop_test, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=5)

        self.clear_button = ttk.Button(control_frame, text="Очистить вывод", command=self.clear_output)
        self.clear_button.grid(row=0, column=2, padx=5)

        self.debug_var = tk.BooleanVar(value=False)
        debug_check = ttk.Checkbutton(control_frame, text="Подробный вывод", variable=self.debug_var)
        debug_check.grid(row=0, column=3, padx=20)

        # Прогресс-бар
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=10)

        # Область статистики
        stats_frame = ttk.LabelFrame(main_frame, text="Статистика", padding="10")
        stats_frame.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        stats_frame.columnconfigure(0, weight=1)
        stats_frame.rowconfigure(0, weight=1)

        self.output_text = scrolledtext.ScrolledText(stats_frame, height=15, width=80, font=('Courier', 9))
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.output_text.tag_config("success", foreground="green")
        self.output_text.tag_config("error", foreground="red")
        self.output_text.tag_config("info", foreground="blue")
        self.output_text.tag_config("title", foreground="purple", font=('Arial', 10, 'bold'))

        # Статусная строка
        self.status_var = tk.StringVar(value="Готов к тестированию")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=5)

    def log(self, message: str, tag=None):
        self.output_text.insert(tk.END, message + "\n", tag)
        self.output_text.see(tk.END)
        self.root.update_idletasks()

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)

    def generate_hex(self) -> str:
        return f"{random.randint(0x0000, 0xFFFF):04X}"

    def run_test(self):
        try:
            num_unique = self.unique_questions_var.get()
            total_ops = self.total_ops_var.get()
            importance_rate = self.importance_var.get()
            memory_size = self.memory_size_var.get()
            new_fact_prob = self.new_fact_prob_var.get()
            verbose = self.debug_var.get()

            self.pixel = PixelMemory(max_size=memory_size)
            self.pixel.set_verbose(verbose)

            # Генерируем базу уникальных вопросов и ответов (все возможные факты)
            # Важные - первые 30%, неважные - остальные
            all_qa_pairs = []
            for i in range(num_unique):
                q = self.generate_hex()
                a = self.generate_hex()
                all_qa_pairs.append((q, a))

            important_count = max(1, int(num_unique * 0.3))
            important_pairs = all_qa_pairs[:important_count]
            non_important_pairs = all_qa_pairs[important_count:]

            # Словарь для быстрого поиска ответа
            answer_dict = dict(all_qa_pairs)

            # Счётчики
            facts_learned = set()  # Какие факты уже были выучены
            questions_asked = 0
            correct_answers = 0
            accuracy_over_time = []
            operations_done = 0

            # Сначала запоминаем небольшое количество фактов (чтобы память не была пустой)
            initial_facts_count = min(memory_size, 5)
            self.log("\n" + "="*80, "title")
            self.log("НАЧАЛО ТЕСТА", "title")
            self.log("="*80, "title")
            self.log(f"\nПараметры:", "info")
            self.log(f"  • База уникальных фактов: {num_unique}", "info")
            self.log(f"  • Важных фактов (первые 30%): {important_count}", "info")
            self.log(f"  • Всего операций: {total_ops}", "info")
            self.log(f"  • Размер памяти: {memory_size}", "info")
            self.log(f"  • Вероятность важного вопроса: {importance_rate:.0%}", "info")
            self.log(f"  • Вероятность нового факта: {new_fact_prob:.0%}", "info")

            self.log(f"\n--- НАЧАЛЬНОЕ ЗАПОЛНЕНИЕ ПАМЯТИ ({initial_facts_count} фактов) ---", "info")
            for i in range(initial_facts_count):
                q, a = all_qa_pairs[i % len(all_qa_pairs)]
                self.pixel.process(f"{q} → {a}")
                facts_learned.add(q)
                self.log(f"  Запомнен: {q} → {a}", "info")

            self.log(f"\n--- ОСНОВНОЙ ЦИКЛ ТЕСТА ({total_ops} операций) ---", "info")

            block_size = max(1, total_ops // 10)  # 10 блоков для статистики
            self.progress_bar["maximum"] = total_ops

            for op_num in range(total_ops):
                if not self.test_running:
                    break

                operations_done += 1

                # Решаем, что делать: новый факт или вопрос
                if random.random() < new_fact_prob:
                    # === НОВЫЙ ФАКТ ===
                    # Выбираем случайный факт из базы, который ещё не выучен
                    available_facts = [(q, a) for q, a in all_qa_pairs if q not in facts_learned]

                    if available_facts:
                        q, a = random.choice(available_facts)
                        self.pixel.process(f"{q} → {a}")
                        facts_learned.add(q)
                        if verbose:
                            self.log(f"[НОВЫЙ ФАКТ] {q} → {a} (всего выучено: {len(facts_learned)})", "info")
                    else:
                        # Все факты уже выучены, тогда задаём вопрос
                        q, a = random.choice(all_qa_pairs)
                        answer = self.pixel.process(q)
                        questions_asked += 1
                        if answer == a:
                            correct_answers += 1
                            if verbose:
                                self.log(f"✓ {q} → {answer} (ПРАВИЛЬНО)", "success")
                        else:
                            self.log(f"✗ {q} → {answer or 'None'} (ожидалось: {a})", "error")
                else:
                    # === ВОПРОС ===
                    # С вероятностью importance_rate задаём важный вопрос, иначе случайный из выученных
                    if random.random() < importance_rate:
                        # Важный вопрос (из первых 30%)
                        candidate_pairs = [(q, a) for q, a in important_pairs if q in facts_learned]
                    else:
                        # Любой выученный вопрос
                        candidate_pairs = [(q, a) for q, a in all_qa_pairs if q in facts_learned]

                    if candidate_pairs:
                        q, expected = random.choice(candidate_pairs)
                        answer = self.pixel.process(q)
                        questions_asked += 1

                        if answer == expected:
                            correct_answers += 1
                            if verbose:
                                self.log(f"✓ {q} → {answer} (ПРАВИЛЬНО)", "success")
                        else:
                            self.log(f"✗ {q} → {answer or 'None'} (ожидалось: {expected})", "error")
                    else:
                        # Нет выученных вопросов - запоминаем новый факт
                        q, a = all_qa_pairs[len(facts_learned) % len(all_qa_pairs)]
                        self.pixel.process(f"{q} → {a}")
                        facts_learned.add(q)
                        if verbose:
                            self.log(f"[ВЫУЧЕНО] {q} → {a}", "info")

                # Периодическая статистика
                if (op_num + 1) % block_size == 0 and questions_asked > 0:
                    current_acc = correct_answers / questions_asked
                    accuracy_over_time.append(current_acc)
                    self.log(f"\n[СТАТИСТИКА] После {op_num+1} операций, {questions_asked} вопросов: "
                            f"{correct_answers}/{questions_asked} = {current_acc:.1%}", "info")
                    self.log(f"  Выучено фактов: {len(facts_learned)}/{num_unique}", "info")
                    self.log(f"  Память: {self.pixel.get_memory_size()}/{memory_size} фактов", "info")

                self.progress_var.set((op_num + 1) / total_ops * 100)
                self.status_var.set(f"Операций: {op_num+1}/{total_ops} | "
                                   f"Вопросов: {questions_asked} | "
                                   f"Точность: {correct_answers/questions_asked if questions_asked>0 else 0:.1%}")
                time.sleep(0.005)

            # Финальные результаты
            self.log("\n" + "="*80, "title")
            self.log("РЕЗУЛЬТАТЫ ТЕСТА", "title")
            self.log("="*80, "title")

            if questions_asked > 0:
                final_acc = correct_answers / questions_asked
                self.log(f"\nИТОГО вопросов: {questions_asked}", "info")
                self.log(f"Правильных ответов: {correct_answers}", "success")
                self.log(f"Итоговая точность: {final_acc:.1%}", "success")
                self.log(f"Всего выучено фактов: {len(facts_learned)}/{num_unique}", "info")
                self.log(f"Размер памяти: {self.pixel.get_memory_size()}/{memory_size}", "info")

                # Анализ тренда
                if len(accuracy_over_time) >= 2:
                    self.log(f"\nДинамика точности по блокам:", "info")
                    for i, acc in enumerate(accuracy_over_time, 1):
                        self.log(f"  Блок {i:2d}: {acc:.1%}", "info")

                    first_acc = accuracy_over_time[0]
                    last_acc = accuracy_over_time[-1]
                    improvement = last_acc - first_acc

                    self.log(f"\nИзменение точности: {improvement:+.1%}", "info")

                    if improvement > 0.03:
                        self.log("\n✅ ВЕРДИКТ: Точность ЗНАЧИТЕЛЬНО УЛУЧШИЛАСЬ!", "success")
                    elif improvement > 0:
                        self.log("\n✅ ВЕРДИКТ: Точность УЛУЧШИЛАСЬ!", "success")
                    elif improvement == 0:
                        self.log("\n✅ ВЕРДИКТ: Точность СТАБИЛЬНА!", "success")
                    else:
                        self.log("\n❌ ВЕРДИКТ: Точность УХУДШИЛАСЬ!", "error")
                else:
                    self.log("\nНедостаточно данных для анализа тренда", "info")
            else:
                self.log("\n⚠️ Вопросов не было задано!", "error")

            self.status_var.set(f"Тест завершён. Точность: {correct_answers/questions_asked if questions_asked>0 else 0:.1%}")

        except Exception as e:
            self.log(f"\nОШИБКА: {e}", "error")
            import traceback
            self.log(traceback.format_exc(), "error")
        finally:
            self.test_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.progress_var.set(0)

    def start_test(self):
        if self.test_running:
            return
        if self.unique_questions_var.get() < 3:
            messagebox.showerror("Ошибка", "Количество уникальных вопросов должно быть не менее 3")
            return
        if self.total_ops_var.get() < 20:
            messagebox.showerror("Ошибка", "Операций должно быть не менее 20")
            return

        self.clear_output()
        self.test_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.progress_var.set(0)

        self.test_thread = Thread(target=self.run_test)
        self.test_thread.daemon = True
        self.test_thread.start()

    def stop_test(self):
        if self.test_running:
            self.test_running = False
            self.log("\nТест остановлен пользователем", "info")
            self.status_var.set("Остановлен")


def main():
    root = tk.Tk()
    app = PixelTestGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()