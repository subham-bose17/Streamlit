import streamlit as st
st.title('Welcome to my st app')
st.header("Header")
st.subheader("subheader")
st.text("Text")
st.write("Write")

mydropdown = st.selectbox('Fruties:',['mango','banana','apple'])
st.write(f'your choose {mydropdown}')
st.success("Selected")

if st.button("Click Here"):
    st.success("Clicked")
    st.error("Error")
    st.warning("Warning")
    st.info("Info")
    st.balloons()
    st.spinner('Loading...')
    st.status('processing...')

tick = st.checkbox("Tick here")
if tick:
    st.write("You are checked")
    st.snow()
    st.progress(80)
    st.toast('Hello user!')

radio = st.radio("pick your choice:",['Thor','Iron man','captain america'])
st.write(f'your choose {radio}')
st.toggle('ON/OFF')
carspeed = st.slider("Car speed :",0,15,10)
st.write(f'your carspeed is {carspeed} ')

st.metric('Temp :', '28 C', '-2 C') 



numinp = st.number_input("Enter a number :",min_value=1,max_value=11,step=2)

name = st.text_input("Enter your name:")
if name :
    st.write(f'Hello {name}')

date = st.date_input("Select Date")

col1, col2 = st.columns(2)

with col1:
    st.header("First")
    st.image("https://images.pexels.com/photos/3798989/pexels-photo-3798989.jpeg", width = 400)
    btn1 = st.button('ClickOne')
with col2:
    st.header("Second")
    st.image("https://images.pexels.com/photos/2387637/pexels-photo-2387637.jpeg", width = 400)
    btn2 = st.button('ClickTwo')

if btn1:
    st.info("Owl")
elif btn2:
    st.info("Monkey")

userName = st.sidebar.text_input("Enter your name:")
location = st.sidebar.selectbox('choose youe location:',['serampore','rishra','hooghly'])
with st.expander("More  locations: ") :
    st.write("""
    1. Darjeeling
    2. digha
    3. Manali
            """)

st.markdown('# Welcome to my js class')
st.markdown("""
## Spread operator (`...`)
- Expands (Spreads) an array or obj into individual elements.
- Used in arrays, objects, and function calls.

### Example :
```javascript
let arr = [1,2,3];
let newArr = [...arr, 4,5];
console.log(newArr);//[1,2,3,4,5] 
```
---
            
            """)

