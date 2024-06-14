import tkinter as tk

class BMICalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de IMC")

        self.label_height = tk.Label(master, text="Altura (m):")
        self.label_height.grid(row=0, column=0)

        self.label_weight = tk.Label(master, text="Peso (kg):")
        self.label_weight.grid(row=1, column=0)

        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=0, column=1)

        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=1, column=1)

        self.calculate_button = tk.Button(master, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2)

        self.label_result = tk.Label(master, text="")
        self.label_result.grid(row=3, column=0, columnspan=2)

    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            bmi = weight / (height ** 2)
            self.label_result.config(text=f"Seu IMC é: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            self.label_result.config(text="Por favor, insira valores válidos para altura e peso.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif bmi < 25:
            category = "Peso normal"
        elif bmi < 30:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        self.label_result.config(text=f"Seu IMC é: {bmi:.2f} - {category}")

def main():
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

