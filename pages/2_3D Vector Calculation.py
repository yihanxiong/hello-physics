import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ..................................Page Header Format Start.......................................................

# .....This page name /str ......
page_str = "3D Vector Calculation"                                                                   # Input
subheader_str = ("This demo illustrates summation(+), substation(-), dot product(.) and "
                 "cross product(X) of two 3D vectors. Enjoy!")                                       # Input

# ...... set page title, page icon and wide screen.....
st.set_page_config(page_title=page_str, page_icon='tada:', layout="wide")

# .....Display this page's sidebar name...............
st.sidebar.header(page_str)

# .....Display this page's name...............
html_str1 = f"""
<style>
p.a {{
  font: bold 60px Arial;
}}
</style>
<p class="a">{page_str}</p>
"""
st.markdown(html_str1, unsafe_allow_html=True)

# .....Display this page's subheader...............
html_str2 = f"""
<style>
p.a {{
  font: bold 25px Arial;
}}
</style>
<p class="a">{subheader_str}</p>
"""
st.markdown(html_str2, unsafe_allow_html=True)

# ..............................Page Header Format End..........................................................


m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #0099ff;
        color:#ffffff;
    }
    div.stButton > button:hover {
        background-color: #00ff00;
        color:#ff0000;
        }
    </style>""", unsafe_allow_html=True)
button = st.button("Run Simulation for Vector Calculation")

# ...... define three columns ........

left_column, mid_column, right_column = st.columns([1, 2, 2])


# ...... left column is the Vector A and B input..........
with left_column:
    st.title("")
    st.title("")
    st.latex(r'''\vec{A}''' + '   Input:')
    Ax = left_column.number_input('Please enter X component of Vector A: ', -1000000000, 1000000000, 14)
    Ay = left_column.number_input('Please enter Y component of Vector A: ', -1000000000, 1000000000, 4)
    Az = left_column.number_input('Please enter Z component of Vector A: ', -1000000000, 1000000000, 5)
    st.title("")
    st.title("")
    st.title("")
    st.latex(r'''\vec{B}''' + '   Input:')
    Bx = left_column.number_input('Please enter X component of Vector B: ', -1000000000, 1000000000, 1)
    By = left_column.number_input('Please enter Y component of Vector B: ', -1000000000, 1000000000, 7)
    Bz = left_column.number_input('Please enter Z component of Vector B: ', -1000000000, 1000000000, 2)

    left_column.markdown(
        """
        <style>

        text {
            font-size: 5rem !important;
        }
        input {
            font-size: 2rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ....... vector calculation............

Sum_x = Ax + Bx
Sum_y = Ay + By
Sum_z = Az + Bz
Minus_x = Ax - Bx
Minus_y = Ay - By
Minus_z = Az - Bz
Dot_product = Ax * Bx + Ay * By + Az * Bz
# .............................youti work on .......................................................
Cross_product_x =
Cross_product_y =
Cross_product_z =

# .......................... A + B figure setting..........................
fig1 = plt.figure(1)
ax = fig1.add_subplot(projection='3d')
ax.quiver(0, 0, 0, Ax, Ay, Az, color='red')
ax.quiver(0, 0, 0, Bx, By, Bz, color='blue')
ax.quiver(0, 0, 0, Sum_x, Sum_y, Sum_z, color='green')
ax.set_xlim(min(0, int(min(Ax,Bx,Sum_x)) - 1), max(0, int(max(Ax,Bx,Sum_x)) + 1))
ax.set_ylim(min(0, int(min(Ay,By,Sum_y)) - 1), max(0, int(max(Ay,By,Sum_y)) + 1))
ax.set_zlim(min(0, int(min(Az,Bz,Sum_z)) - 1), max(0, int(max(Az,Bz,Sum_z)) + 1))
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Two Vector Summation')
ax.text(Ax, Ay, Az, "A", color='red')
ax.text(Bx, By, Bz, "B", color='blue')
ax.text(Sum_x, Sum_y, Sum_z, "A+B", color='green')

# .......................... A - B figure setting..........................
fig2 = plt.figure(2)
ax = fig2.add_subplot(projection='3d')
ax.quiver(0, 0, 0, Ax, Ay, Az, color='red')
ax.quiver(0, 0, 0, Bx, By, Bz, color='blue')
ax.quiver(0, 0, 0, Minus_x, Minus_y, Minus_z, color='green')
ax.set_xlim(min(0, int(min(Ax,Bx,Minus_x)) - 1), max(0, int(max(Ax,Bx,Minus_x)) + 1))
ax.set_ylim(min(0, int(min(Ay,By,Minus_y)) - 1), max(0, int(max(Ay,By,Minus_y)) + 1))
ax.set_zlim(min(0, int(min(Az,Bz,Minus_z)) - 1), max(0, int(max(Az,Bz,Minus_z)) + 1))
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Two Vector Substraction')
ax.text(Ax, Ay, Az, "A", color='red')
ax.text(Bx, By, Bz, "B", color='blue')
ax.text(Minus_x, Minus_y, Minus_z, "A-B", color='green')

# .......................... A dot B figure setting..........................
# .......................... A Cross B figure setting..........................


# ..............................Latex to write Vector function .............
def latexVector(Ax, Ay, Az, Bx, By, Bz, oper):     # oper = "Sum"/ "Minus" 5/ "Dot" / "Cross"
    A_vec_str = (r'''\vec{A}''' + ' = ' + rf'''{Ax} ''' + r'''\vec{X} + ''' + rf'''{Ay} ''' + r'''\vec{Y} + '''
                          + rf'''{Az} ''' + r'''\vec{Z}''')
    B_vec_str = (r'''\vec{B}''' + ' = ' + rf'''{Bx} ''' + r'''\vec{X} + ''' + rf'''{By} ''' + r'''\vec{Y} + '''
                          + rf'''{Bz} ''' + r'''\vec{Z}''')
    sum_vec_str = (r'''\vec{A}''' + ' + ' + r'''\vec{B}''' + ' = ' + rf'''{Sum_x} ''' + r'''\vec{X} + '''
                           + rf'''{Sum_y} ''' + r'''\vec{Y} + ''' + rf'''{Sum_z} ''' + r'''\vec{Z}''')
    minus_vec_str = (r'''\vec{A}''' + ' - ' + r'''\vec{B}''' + ' = ' + rf'''{Minus_x} ''' + r'''\vec{X} + '''
                           + rf'''{Minus_y} ''' + r'''\vec{Y} + ''' + rf'''{Minus_z} ''' + r'''\vec{Z}''')
    dot_scalar_str = (r'''\vec{A}''' + ' . ' + r'''\vec{B}''' + ' =  AxBx + AyBy + AzBz = ' + rf'''{Dot_product}''')

    if oper == "Sum":
        return st.latex(A_vec_str), st.latex(B_vec_str), st.latex(sum_vec_str)
    elif oper == "Minus":
        return st.latex(A_vec_str), st.latex(B_vec_str), st.latex(minus_vec_str)
    elif oper == "Dot":
        return st.latex(A_vec_str), st.latex(B_vec_str), st.latex(dot_scalar_str)
    elif oper == "Cross":
        return st.latex(A_vec_str), st.latex(B_vec_str)
    else:
        return "Invalid"
# ..............................................................................

.0

if button:
    with mid_column:
        st.title("")
        st.title("")
        st.write(fig1)
        latexVector(Ax, Ay, Az, Bx, By, Bz, "Sum")

        # .............................youti work on .......................................................
        # display A . B

    # ..... A - B  plot........
    with right_column:
        st.title("")
        st.title("")
        st.write(fig2)
        latexVector(Ax, Ay, Az, Bx, By, Bz, "Minus")
        # .............................youti work on .......................................................
        # display A X B