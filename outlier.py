
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import statistics
import seaborn as sns

st.set_page_config('Outlier', '🌟', layout='centered')


st.subheader('🎯 Effect of outliers on mean, median, and mode.')

st.success("Move the slider to explore how an outlier influences statistical measures.")

# Slider for Outlier set by user
with st.sidebar.container(border=True):
# with st.sidebar:
    outlier_value = st.slider("Outlier's Value", min_value=0, max_value=100, value = 23)
    
age = [19, 20, 21, 22, 22, outlier_value]
name = ['John', 'Jasi','Abey','Abhik','Piku','Outlier']
mean_value = np.mean(age)
median_value = np.median(age)
mode_value = statistics.mode(age)



# Display value of Mean, Median, and Mode
with st.sidebar.container(border=True):
    col1, col2, col3 = st.columns(3)
    col1.markdown(f'**Mean** {mean_value:.2f}')
    col2.markdown(f'**Median** {median_value:.2f}')
    col3.markdown(f'**Mode** {mode_value:.2f}')


st.sidebar.markdown("### 📊 Dataset Preview")
st.sidebar.dataframe({"Name": name, "Age": age})


# Display the graph
fig = plt.figure(figsize = (7,4))
plt.plot( name, age, marker = 'o', linestyle='-', color='black')
plt.axhline(mean_value, color='green', linestyle='--', linewidth=1.5, label='Mean')
plt.axhline(median_value, color='red', linestyle='--', label ='Median')
plt.axhline(mode_value, color='skyblue', label='Mode')
plt.title('Line Plot with Mean, Median, Mode')
plt.xlabel('Name of the person')
plt.ylabel('Age')
plt.legend()
plt.grid(True)
st.pyplot(fig)


# Key Takeaways
expand = st.expander("Key Takeaways:", icon=":material/info:")
expand.markdown(
"""
**Without Outlier:**
- Mean, median, and mode are close together.

**With Outlier:**
- Mean increases/decreases significantly (sensitive to outlier).
- Median changes slightly or stays the same.
- Mode usually stays unchanged, especially for repeated values.
"""
)

# Mean 
expand = st.expander("Mean", icon=":material/info:")
expand.markdown(
"""
The mean is a measure of central tendency that represents the average value of a dataset. 
It is calculated by summing all the observations and dividing by the number of observations.
"""
)

# Median 
expand = st.expander("Median", icon=":material/info:")
expand.markdown(
"""
The median is the middle value in a dataset when the values are arranged in ascending or descending order. 
It is a measure of central tendency that is less affected by outliers than the mean.

**Calculation to find Median:**
1. Sort the data in order.

2. If the number of values (n) is:
    - Odd: Median is the middle value.
    - Even: Median is the average of the two middle values.

**Importance of Median:**  
    - It gives a better central value when the data has outliers or is skewed.  
    - It represents the 50th percentile (half the values are below, half above).
"""
)

# Mode
expand = st.expander("Mode", icon=":material/info:")
expand.markdown(
"""
The mode is the value that appears most frequently in a dataset. It is another measure of central tendency.

**A dataset can have:**

- One mode → Unimodal
- Two modes → Bimodal
- More than two modes → Multimodal
- No mode → if all values appear only once

**Importance of Mode:**   
- Helpful for categorical data (e.g., most common color, brand, etc.)
- Not affected by outliers
- May not exist or may not be unique in all datasets

"""
)

# Summary
expand = st.expander("Summary", icon=":material/info:")
expand.markdown(
""" 
| Metric | Sensitive to Outliers? | Explanation                                   |
| ------ | ---------------------- | --------------------------------------------- |
| Mean   | ✅ Yes                  | Outlier increases/decreases the average significantly.  |
| Median | ❌ No                   | It’s based on middle value — more stable.     |
| Mode   | ❌ Usually No           | May remain same unless outlier repeats often. |

"""
)


#---------------------------------------------------------
# Footer
#----------------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<hr style="margin-top: 30px;">
<div style="text-align: center; font-size: 0.9em; color: gray;">
    Created by <b>Partho Sarothi Das</b><br>
    <i>Aspiring Data Scientist | Passionate about ML & Visualization</i><br>
    Email: <a href="mailto:partho52@gmail.com">partho52@gmail.com</a>
</div>
""", unsafe_allow_html=True)