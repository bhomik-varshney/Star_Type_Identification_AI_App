import streamlit
import streamlit as st
import pandas as pd
import ai_model
from ai_model import data, load_model,working_data
import matplotlib.pyplot as plt
import seaborn as sns

# st.html(f"""<p style = "font-size:50px"># Star Type Identification</p>""")
st.title('''# Star Type Identification :moon:''')
st.caption("Powered by A.I.")


my_data = ai_model.data()
train_data = ai_model.working_data()
model = load_model()

with st.sidebar:
    st.title("Enter The Insights")
    temp = st.number_input("Temperature ( K )",min_value=0,max_value=1000000,step=1)
    if(temp>40000 or temp<1000):
        st.error("Temperature value is out of scope")
    absolute_luminosity = st.number_input("Luminosity ( Watts , /10^26)", min_value=0.00, max_value=5000000.00, step=0.01)
    if (absolute_luminosity > 3500000):
        st.error("Absolute Luminosity value is out of scope")
    st.caption('''Please write the value as :-
             absolute luminosity (in Watts) divided by 10^26.''')
    absolute_radius = st.number_input("Radius ( M )",min_value=0.00,max_value=50000.00,step=0.01)
    if (absolute_radius > 15000):
        st.error("Absolute Radius value is out of scope")
    st.caption('''Please write the value as :-
                 absolute Radius (in Metres) divided by 10^8.''')
    absolute_magnitude = st.number_input("Absolute Magnitude (Mv) ",min_value=-50.00,max_value=50.00,step=0.01)
    if (absolute_magnitude > 20 or absolute_magnitude<-12):
        st.error("Absolute Magnitude value is out of scope")
    color = st.selectbox("Color",["Red","Blue","White","Yellow","Orange","Orange-Red","Blue-White","Yellow-White"])
    spectral_class = st.selectbox("Spectral Class",["M","B","O","A","F","K","G"])

relative_luminosity = absolute_luminosity/3.828
relative_radius = absolute_radius/6.9551
def color_encoder(color):
    if(color == "Red"):
        return 1
    elif(color == "Blue"):
        return 2
    elif(color== "White"):
        return 5
    elif(color=="Yellow"):
        return 6

    elif (color == "Orange"):
        return 7
    elif (color == "Orange-Red"):
        return 8
    elif(color == "Blue-White"):
        return 3
    elif(color=="Yellow-White"):
        return 4

def spectral_encoder(spectral_class):
    if(spectral_class == "M"):
        return 1
    elif(spectral_class=="B"):
        return 2
    elif(spectral_class=="O"):
        return 3
    elif(spectral_class=="A"):
        return 4
    elif(spectral_class=="F"):
        return 5
    elif(spectral_class=="K"):
        return 6
    elif(spectral_class=="B"):
        return 7

input_data = {
    'Temperature': temp,
    'L': relative_luminosity,
    'R': relative_radius,
    'A_M':absolute_magnitude,
    'Color': color_encoder(color),
    'Spectral_Class' : spectral_encoder(spectral_class)
}
input_data2 = {
    'Temperature': temp,
    'L': relative_luminosity,
    'R': relative_radius,
    'A_M':absolute_magnitude,
    'Color': color,
    'Spectral_Class' : spectral_class
}

input_df = pd.DataFrame(input_data, index=[1])
input_df2 = pd.DataFrame(input_data2,index=[1])

def prediction_decoder(prediction):
    if(prediction==0):
        return "Red Dwarf"
    elif(prediction==1):
        return "Brown Dwarf"
    elif(prediction == 2):
        return "White Dwarf"
    elif(prediction==3):
        return "Main Sequence"
    elif(prediction ==4):
        return "Super Giant"
    elif(prediction == 5):
        return "Hyper Giant"
    else:
        return "Unable to classify the Star"

prediction = model.predict(input_df)
predicted_Type = prediction_decoder(prediction)
st.write("")
st.header("-> Model")
st.caption("Given Input Data")
st.table(input_df2)
#rgb(25, 135, 84)
st.markdown(f"""
<div style='text-align: center; background-color:  rgb(255, 215, 0); padding: 10px; border-radius: 10px; color:white;padding-top:30px;padding-bottom:30px;'>
    <span style='font-size: 30px; font-weight: bold'>{predicted_Type}</span>
</div>
""", unsafe_allow_html=True)
st.write("")

# Add custom CSS to change the hover color of the expander text and arrow to match st.info() color
st.markdown("""
    <style>
    /* Change the text color of the expander to the info color on hover */
    details summary:hover {
        color: #17a2b8 !important;  /* Info box blue color */
    }

    /* Change the color of the expander arrow to the info color on hover */
    details summary:hover div[role="button"]::before {
        color: #17a2b8 !important;  /* Info box blue color */
    }

    /* Ensure the arrow stays the info color when the expander is open */
    details[open] summary div[role="button"]::before {
        color: #17a2b8 !important;  /* Info box blue color for the arrow when expanded */
    }
    </style>
""", unsafe_allow_html=True)


if (predicted_Type=="Red Dwarf"):
    st.html(f"""<details>
    <h2></h2>
            <summary>Wanna know about Red Dwarfs ?</summary>
            <div style="background-color: rgb(38, 139, 210); color: white; padding: 10px;border-radius:10px;padding-top:15px">
            <p><h2> Overview</h2>
    Red dwarfs are the most common type of star in the universe. They are small, cool, and faint compared to other types of stars like the Sun. Here's an in-depth look at their characteristics:
    
    <h3>Key Characteristics</h3>
    <h4>1. Size and Mass:</h4>
    Red dwarfs are the smallest stars in the main sequence, with masses ranging from about 0.08 to 0.6 times the Sun's mass.
    Their radii are also smaller, about 20% to 50% of the Sun's radius.
    <h4>2. Temperature:</h4>
    Surface temperatures are relatively cool, ranging between 2,500 K and 4,000 K.
    Their cooler temperatures give them a reddish color, hence the name "red dwarf."
    <h4>3. Brightness:</h4>
    Red dwarfs are faint, emitting 0.01% to 10% of the Sun's luminosity.
    Their faintness makes them hard to detect with the naked eye, despite being numerous.
    <h4>4. Lifespan:</h4>
    Red dwarfs have exceptionally long lifespans, often trillions of years.
    They burn hydrogen slowly due to their low mass, meaning they stay in the main sequence phase for much longer than larger stars.
    <h3>Notable Features</h3>
    <h4>1. Activity:</h4>
    Some red dwarfs are known for being active stars, with strong stellar flares and magnetic activity.
    <h4>2. Habitability:</h4>
    Planets orbiting red dwarfs are of great interest in the search for extraterrestrial life due to their long stable lifetimes.
    However, their habitable zones are close to the star, exposing planets to stellar radiation and tidal locking.
    <h4>3. Examples of Red Dwarfs:</h4>
    <b>* Proxima Centauri:</b> The closest star to the Sun and part of the Alpha Centauri system.
    <b>* Barnard's Star:</b> A well-studied red dwarf known for its rapid motion across the sky.
    </p>
            </div>
        </details>""")
elif(predicted_Type=="Brown Dwarf"):
    st.html(f"""<details>
        <h2></h2>
                <summary>Wanna know about Brown Dwarfs ?</summary>
                <div style="background-color: rgb(38, 139, 210); color: white; padding: 10px;border-radius:10px;padding-top:15px">
                <p><h2>Overview</h2>
Brown dwarfs are fascinating celestial objects that sit between the largest planets and the smallest stars. Often referred to as "failed stars," they lack the mass required to sustain nuclear fusion in their cores, which is the defining process of true stars.

<h3>Key Characteristics</h3>
<h4>1. Size and Mass:</h4>
Brown dwarfs are larger than gas giant planets like Jupiter but smaller than the smallest stars.
Their mass ranges from about 13 to 80 times the mass of Jupiter (approximately 0.01 to 0.08 solar masses).
<h4>2. Temperature:</h4>
Surface temperatures range from 500 K to 2,500 K, making them cooler than stars.
They emit mostly in the infrared spectrum due to their low temperatures.
<h4>3. Brightness:</h4>
Brown dwarfs are very dim and not visible to the naked eye.
They emit light primarily as residual heat from their formation rather than through nuclear fusion.
<h4>4. Lifespan:</h4>
Brown dwarfs gradually cool and dim over billions of years, as they do not have a sustained energy source like hydrogen fusion.
<h3>Notable Features</h3>
<h4>1. Failed Fusion:</h4>
Brown dwarfs cannot sustain hydrogen fusion in their cores due to insufficient mass.
However, those at the higher end of the mass range can fuse deuterium (a heavy isotope of hydrogen) during their early stages.
<h4>2. Atmospheres:</h4>
They often have complex atmospheres with clouds made of metal oxides, silicates, or even rain composed of molten iron.
<h4>3. Habitability and Planets:</h4>
Some brown dwarfs host planetary systems.
Their low brightness makes it easier to study orbiting planets compared to stars.
<h4>4. Classification:</h4>
Brown dwarfs are classified into spectral types L, T, and Y, based on their temperature and spectral features.
<h4>5. Notable Brown Dwarfs:</h4>
<b>* WISE 0855−0714:</b>
One of the coldest known brown dwarfs, with a temperature around 250 K.
<br>
<b>* Gliese 229B:</b>
A well-studied companion to the red dwarf Gliese 229, showcasing methane absorption lines typical of cooler brown dwarfs.
<br>
<b>* Teide 1:</b>
The first confirmed brown dwarf, discovered in 1995.
</p>
                </div>
            </details>""")
elif(predicted_Type=="White Dwarf"):
    st.html(f"""<details>
        <h2></h2>
                <summary>Wanna know about White Dwarfs ?</summary>
                <div style="background-color: rgb(38, 139, 210); color: white; padding: 10px;border-radius:10px;padding-top:15px">
                <p><h2>Overview</h2>
White dwarfs are the remnants of low-to-medium-mass stars that have exhausted their nuclear fuel. These stellar remnants are incredibly dense and represent the final evolutionary stage of such stars.

<h3>Key Characteristics</h3>
<h4>1. Size and Mass:</h4>
White dwarfs are very small, with a radius comparable to that of Earth (~7,500 km).
Despite their size, they are extremely dense, with a mass close to that of the Sun (~0.6 to 1.4 solar masses).
<h4>2. Temperature:</h4>
Newly formed white dwarfs are extremely hot, with surface temperatures ranging from 10,000 K to 100,000 K.
Over billions of years, they gradually cool as they radiate away their residual heat.
<h4>3. Brightness:</h4>
White dwarfs are faint compared to main-sequence stars, as they emit no energy from fusion, only thermal radiation.
<h4>4. Density and Gravity:</h4>
White dwarfs are incredibly dense; a teaspoon of their material would weigh tons on Earth.
Their surface gravity is around 100,000 times stronger than Earth's gravity.
<h3>5.Notable Features</h3>
<h4>1. Formation:</h4>
White dwarfs form after a star like the Sun exhausts its nuclear fuel, expels its outer layers as a planetary nebula, and leaves behind a dense core.
<h4>2. Degeneracy Pressure:</h4>
White dwarfs are supported against gravitational collapse by electron degeneracy pressure, a quantum mechanical effect.
<h4>3. Chandrasekhar Limit:</h4>
The maximum mass of a white dwarf is 1.4 solar masses. Beyond this, it can no longer be supported by electron degeneracy pressure and may collapse into a neutron star or explode as a supernova.
<h4>4. Cooling Process:</h4>
White dwarfs cool and fade over billions of years, eventually becoming black dwarfs (a theoretical stage, as the universe is not old enough for this to have occurred yet).
<h4>5. Notable White Dwarfs:</h4>
<b>* Sirius B:</b>
The closest and one of the most well-known white dwarfs, orbiting the bright star Sirius.
<br>
<b>* Procyon B:</b>
A faint white dwarf companion to the star Procyon.
<br>
<b>* Van Maanen's Star:</b>
A nearby solitary white dwarf.
</p>
                </div>
            </details>""")
elif(predicted_Type=="Main Sequence"):
    st.html(f"""<details>
        <h2></h2>
                <summary>Wanna know about  Main Sequence ?</summary>
                <div style="background-color: rgb(38, 139, 210); color: white; padding: 10px;border-radius:10px;padding-top:15px">
                <p><h2>Detailed Information</h2>
The main sequence refers to a phase in a star's life cycle where it is fusing hydrogen into helium in its core, which is the dominant process driving its energy output. This stage makes up the majority of a star’s life, and stars can remain in this phase for millions to billions of years, depending on their mass.

<h3>Key Characteristics:</h3>
<h4>1. Position on the Hertzsprung-Russell Diagram (H-R Diagram):</h4>
The main sequence forms a diagonal band on the H-R diagram, running from the upper-left corner (hot, massive stars) to the lower-right corner (cool, low-mass stars).
Stars on the main sequence are classified according to their spectral type (O, B, A, F, G, K, M) and their luminosity.
<h4>2. Hydrogen Fusion:</h4>
During the main sequence phase, stars are primarily powered by nuclear fusion, where hydrogen atoms in the core are fused into helium, releasing large amounts of energy in the form of light and heat.
This fusion process stabilizes the star because the pressure from the energy released balances the inward gravitational pull.
<h4>3. Stellar Classification:</h4>
Massive Stars (O-type, B-type): These are much hotter, brighter, and larger than the Sun, but they burn their hydrogen fuel at a much faster rate. They have lifespans of a few million years.
<br>
Medium Stars (A-type, F-type, G-type, like our Sun): These stars are less massive and have a longer life expectancy. For instance, the Sun is a G-type star and will spend about 10 billion years on the main sequence.
<br>
Low-Mass Stars (K-type, M-type): These are the coolest and least luminous stars, often called red dwarfs. They burn hydrogen very slowly and can remain on the main sequence for tens to hundreds of billions of years.
<h4>4. Core and Energy Production:</h4>
The core of a main sequence star is extremely hot (millions of degrees Celsius) and under high pressure, allowing for the fusion of hydrogen into helium.
The energy produced in the core creates an outward pressure that counteracts gravity, keeping the star stable.
<h4>5. Duration of Main Sequence Phase:</h4>
The main sequence phase varies greatly depending on a star’s mass.
Massive stars burn through their hydrogen quickly and have a main sequence lifespan of only a few million years.
Sun-like stars have a main sequence lifespan of about 10 billion years.
Low-mass stars (red dwarfs) have main sequence lifetimes that can extend into the trillions of years.
<h4>6. Examples:</h4>
<b>* Sun:</b> The Sun is currently in the middle of its main sequence phase. It is expected to remain in this phase for about 10 billion years in total, of which roughly 5 billion years have passed.
<br>
<b>* Alpha Centauri A:</b> A G-type star like the Sun, also on the main sequence.
<br>
<b>* Sirius:</b> An A-type star, more massive and hotter than the Sun, with a much shorter main sequence lifetime.
<h4>7. End of Main Sequence:</h4>
As stars exhaust their hydrogen fuel in the core, they move off the main sequence. For stars like the Sun, they will transition into the red giant phase, where the core contracts and the outer layers expand.
For more massive stars, they may go through supergiant phases and eventually end their lives in supernova explosions.
</p>
                </div>
            </details>""")
elif(predicted_Type=="Super Giant"):
    st.html(f"""<details>
        <h2></h2>
                <summary>Wanna know about  ?</summary>
                <div style="background-color: rgb(38, 139, 210); color: white; padding: 10px;border-radius:10px;padding-top:15px">
                <p><h2>Detailed Information</h2>
Supergiants are a type of star that are much larger and more luminous than the Sun. They are in a later stage of stellar evolution, typically having exhausted the hydrogen in their cores and undergoing fusion of heavier elements. Supergiants can be found in both the red and blue parts of the H-R diagram, depending on their temperature and size.

<h3>Key Characteristics:</h3>
<h4>1. Position on the Hertzsprung-Russell Diagram (H-R Diagram):</h4>
Supergiants are located in the upper-right portion of the H-R diagram. These stars are among the most luminous and largest stars in the universe.
They can be classified into two main categories based on their color:
<h4>2. Red Supergiants:</h4> Cooler, with lower surface temperatures (around 3,000-4,000 K), but extremely large and luminous.
<h4>3. Blue Supergiants:</h4> Hotter, with surface temperatures above 10,000 K, and typically more massive than red supergiants.
<h4>4. Size and Luminosity:</h4>
Supergiants are very large stars, with radii up to 1,000 times that of the Sun, and they can be thousands to tens of thousands of times more luminous than the Sun.
Due to their immense size and luminosity, they can be seen from vast distances, even though they may only last for a short period of time in stellar terms.
<h4>5. Fusion of Heavier Elements:</h4
Supergiants have passed through the main sequence and the red giant phase. At this stage, their cores are hot enough to fuse elements heavier than hydrogen, such as helium, carbon, oxygen, and even elements like silicon and iron in later stages.
This fusion of heavier elements allows them to continue shining brightly, but they also evolve rapidly due to the instability of the fusion process at such advanced stages.
<h4>6. Short Lifespan:</h4>
Despite their enormous size and brightness, supergiants have very short lifespans compared to smaller stars. A supergiant may only spend a few million years in this phase. This is because their fuel is used up much faster due to their higher fusion rates.
The more massive a star is, the shorter its life. Supergiants may live for only around 10 to 20 million years before exhausting their nuclear fuel.
<h4>7. Mass and Evolution:</h4>
Supergiants typically have masses ranging from about 10 to 50 times that of the Sun. More massive stars may begin their lives as blue supergiants, while less massive ones might eventually become red supergiants.
The evolution from a main sequence star to a supergiant involves the star’s core contracting and heating up, while its outer layers expand and cool.
<h4>8. Examples of Supergiants:</h4>
<b>* Betelgeuse (Red Supergiant):</b> One of the most famous red supergiants, located in the constellation Orion. It is about 700 times the size of the Sun and is expected to explode as a supernova within the next 100,000 years.
<br>
<b>* Rigel (Blue Supergiant):</b> A blue supergiant in the constellation Orion. It is about 1,000 times more luminous than the Sun and has a surface temperature of around 12,000 K.
<br>
<b>* Antares (Red Supergiant):</b> A red supergiant in the constellation Scorpius, about 10 times more massive than the Sun.
<h4>9. End of Life:</h4>
Supergiants end their lives in a supernova explosion, which is one of the most powerful events in the universe. The core may collapse into a neutron star or, in the case of very massive stars, into a black hole.
The supernova expels the outer layers of the star, enriching the interstellar medium with heavy elements that are essential for the formation of new stars, planets, and even life.
</p>
                </div>
            </details>""")
elif(predicted_Type=="Hyper Giant"):
    st.html(f"""<details>
        <h2></h2>
                <summary>Wanna know about Hyper Giants ?</summary>
                <div style="background-color: rgb(38, 139, 210); color: white; padding: 10px;border-radius:10px;padding-top:15px">
                <p><h2>Detailed Information</h2>
Hypergiants are among the most massive and luminous stars in the universe. They represent an even more extreme evolutionary stage than supergiants, with their mass, size, and luminosity reaching extraordinary values. Hypergiants are incredibly rare and are typically at the upper limit of stellar evolution.

<h3>Key Characteristics:</h3>
<h4>1. Position on the Hertzsprung-Russell Diagram (H-R Diagram):</h4>
Hypergiants are located at the very top of the H-R diagram, above the supergiants. These stars are the largest and brightest, with luminosities thousands to tens of thousands of times greater than that of the Sun.
Like supergiants, hypergiants can be either red or blue, depending on their temperature and mass, but their extreme size and energy output distinguish them from other large stars.
<h4>2. Size and Luminosity:</h4>
Hypergiants can have radii up to 1,000 times the Sun’s radius or more, with some estimates putting them as large as 2,000-3,000 times the size of the Sun.
Their luminosities are tens of thousands to hundreds of thousands of times more than the Sun, making them some of the brightest stars in the universe.
<h4>3. Massive and Short-Lived:</h4>
Hypergiants typically have masses ranging from 50 to 100 times the mass of the Sun or even higher. However, this extreme mass leads to an accelerated rate of nuclear fusion, causing them to burn their fuel rapidly.
As a result, hypergiants have extremely short lifespans—just a few million years—before they exhaust their nuclear fuel and undergo dramatic evolutionary changes.
<h4>4. Fusion and Instability:</h4>
Hypergiants are at the pinnacle of the fusion process, having moved through the stages of hydrogen fusion into heavier elements. As they age, they may begin fusing elements such as carbon, oxygen, and silicon in their cores.
Their extreme mass and energy output create tremendous internal pressure and high temperatures, leading to significant stellar instability. Hypergiants often experience large fluctuations in size and brightness, including dramatic mass loss through stellar winds, which can expel a significant portion of their outer layers into space.
<h4>5. Variable Stars:</h4>
Many hypergiants are variable stars, meaning their luminosity fluctuates over time. These variations can be caused by changes in their internal fusion processes, as well as the shedding of material in powerful stellar winds.
For example, some hypergiants are pulsating variable stars, where the star expands and contracts, leading to periodic changes in brightness.
<h4>6. Examples of Hypergiants:</h4>
* <b>VY Canis Majoris:</b> One of the largest and most luminous stars known, located in the constellation Canis Major. It is a red hypergiant and has a radius about 1,500 times that of the Sun, though it is thought to have a relatively short lifespan of just a few million years.
<br>
<b>* WOH G64:</b> A red hypergiant located in the Large Magellanic Cloud, it is one of the largest known stars by volume, with an estimated radius about 2,000 times that of the Sun.
<br>
<b>* Eta Carinae:</b> A famous and highly massive star system in the constellation Carina, which includes one of the most massive known stars. It is a variable star and is considered a luminous blue variable (LBV), transitioning through massive instability.
<h4>7. End of Life:</h4>
Hypergiants have a catastrophic end. After exhausting their fuel, they may undergo a supernova explosion, one of the most powerful events in the universe. The explosion of a hypergiant is often so intense that it can outshine an entire galaxy for a short time.
In cases where the star is sufficiently massive, the core collapse may lead to the formation of a black hole, while less massive hypergiants may collapse into neutron stars.
The death of hypergiants contributes to the creation of heavy elements, which are expelled into the interstellar medium during the supernova explosion, enriching the surrounding environment with the building blocks for new stars and planets.
<h3>Summary of Hypergiant Characteristics:</h3>
<h4>1. Fusion Process:</h4> Fusion of hydrogen and increasingly heavier elements (helium, carbon, oxygen, silicon).
<h4>2. Energy Source:</h4> Extreme fusion rates due to the star's massive size.
<h4>3. Position on H-R Diagram:</h4> Located above supergiants, at the top of the diagram, representing the most luminous stars.
<h4>4. Lifespan:</h4> Very short, just a few million years, due to their high mass and rapid fuel consumption.
<h4>5. Key Examples:</h4> VY Canis Majoris (red hypergiant), WOH G64 (red hypergiant), Eta Carinae (luminous blue variable star).
<h3>Hypergiants are a brief but spectacular stage in stellar evolution. Their extreme luminosity and mass, coupled with their rapid consumption of fuel, make them some of the most fascinating and important objects in understanding the life cycle of massive stars and the evolution of galaxies.</h3></p>
                </div>
            </details>""")
else:
    st.html(f"""<details>
            <h2></h2>
                    <summary>Click to Expand</summary>
                    <div style="background-color: rgb(38, 139, 210); color: white; padding: 10px;border-radius:10px;padding-top:15px">
                    <p> Sorry ! No Information Available </p>
                    </div>
                </details>""")



st.header("-> About this App",anchor="hello")
st.markdown(f"""Welcome to the Star Type Identification app! This application is designed to help users learn about and classify different types of stars in the universe. Using scientific principles and astrophysical data, the app guides you through identifying stars such as main sequence stars, red giants, white dwarfs, supergiants, and more.""")
st.subheader("About the Author")
st.html(f"""
<h3>Hi, I'm <h3 style = "color:#17a2b8">Bhomik Varshney</h3></h3> A passionate Computer Engineering student at Aligarh Muslim University. My journey in AI and data science began with a fascination for unraveling complex patterns in data. This app, Star Type Identification, is a culmination of my love for astronomy and machine learning.
I enjoy building tools that make scientific exploration accessible and engaging. In 2024, I won a hackathon on National Space Day for developing a predictive model for celestial objects.
Through this app, I hope to inspire curiosity about the universe and empower users with easy-to-use tools for star identification.
Let's connect! Find me on <a href = "https://www.linkedin.com/in/bhomik-varshney-a8860a281/">LinkedIn</a> or check out my projects on <a href = "https://github.com/bhomik-varshney">GitHub.</a>""")
st.subheader("Purpose")
st.markdown("The purpose of this app is to make star classification accessible to everyone, whether you're a budding astronomer, a student, or just someone curious about the cosmos.")
st.subheader("Acknowledgments")
st.markdown("We extend our gratitude to Kaggle and NASA for providing the stellar data that powers this app.")
st.subheader("Future Enhancements")
st.markdown("We plan to incorporate real-time stellar observations, advanced visualizations, and AI-driven tools for deeper astronomical insights.")
st.write("")


st.header("-> Dataset")
st.caption("Dear User ! **L** represents *Relative Luminosity* and **R** represents *Relative Radius* of the star")
st.write(my_data)
st.header("-> Data Analytics")
st.line_chart(my_data,x="R",y="Type",x_label="Relative Radius")
st.bar_chart(my_data,x="L",y="Type",x_label="Relative Luminosity")
fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(train_data.corr(),cmap = 'RdYlGn',annot=True,annot_kws ={'size':20},linewidths=0.2,ax=ax)
st.pyplot(fig)









