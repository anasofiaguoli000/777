%%writefile app.py

import streamlit as st
import math

st.title("📐 Cálculo de Área y Perímetro")

st.write("Selecciona una figura para calcular su área y perímetro.")

figura = st.selectbox(
    "Selecciona una figura:",
    ["Rectángulo", "Cuadrado", "Triángulo", "Círculo", "Paralelogramo"]
)

if figura == "Rectángulo":

    st.header("▭ Rectángulo")

    st.write("Área = base × altura")
    st.write("Perímetro = 2 × (base + altura)")

    base = st.number_input("Ingresa la base:", min_value=0.0)
    altura = st.number_input("Ingresa la altura:", min_value=0.0)

    if st.button("Calcular"):
        area = base * altura
        perimetro = 2 * (base + altura)

        st.success(f"Área: {area:.2f} unidades²")
        st.success(f"Perímetro: {perimetro:.2f} unidades")


elif figura == "Cuadrado":

    st.header("□ Cuadrado")

    st.write("Área = lado²")
    st.write("Perímetro = 4 × lado")

    lado = st.number_input("Ingresa el lado:", min_value=0.0)

    if st.button("Calcular"):
        area = lado ** 2
        perimetro = 4 * lado

        st.success(f"Área: {area:.2f} unidades²")
        st.success(f"Perímetro: {perimetro:.2f} unidades")


elif figura == "Triángulo":

    st.header("△ Triángulo")

    st.write("Área = (base × altura) / 2")
    st.write("Perímetro = lado 1 + lado 2 + lado 3")

    base = st.number_input("Ingresa la base:", min_value=0.0)
    altura = st.number_input("Ingresa la altura:", min_value=0.0)
    lado1 = st.number_input("Ingresa el lado 1:", min_value=0.0)
    lado2 = st.number_input("Ingresa el lado 2:", min_value=0.0)
    lado3 = st.number_input("Ingresa el lado 3:", min_value=0.0)

    if st.button("Calcular"):
        area = (base * altura) / 2
        perimetro = lado1 + lado2 + lado3

        st.success(f"Área: {area:.2f} unidades²")
        st.success(f"Perímetro: {perimetro:.2f} unidades")


elif figura == "Círculo":

    st.header("○ Círculo")

    st.write("Área = π × radio²")
    st.write("Perímetro = 2 × π × radio")

    radio = st.number_input("Ingresa el radio:", min_value=0.0)

    if st.button("Calcular"):
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio

        st.success(f"Área: {area:.2f} unidades²")
        st.success(f"Perímetro: {perimetro:.2f} unidades")


elif figura == "Paralelogramo":

    st.header("▱ Paralelogramo")

    st.write("Área = base × altura")
    st.write("Perímetro = 2 × (base + lado)")

    base = st.number_input("Ingresa la base:", min_value=0.0)
    altura = st.number_input("Ingresa la altura:", min_value=0.0)
    lado = st.number_input("Ingresa el lado:", min_value=0.0)

    if st.button("Calcular"):
        area = base * altura
        perimetro = 2 * (base + lado)

        st.success(f"Área: {area:.2f} unidades²")
        st.success(f"Perímetro: {perimetro:.2f} unidades")
