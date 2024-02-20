# PioneerHacksV

We are very excited to present our product SKIB for the PioneerHacks V Hackathon! Here's a detailed description of SKIB's objective and implementation.

### Mission
Our mission is to ensure everyone is able to develop their communication skills so they can express their ideas clearly.

### Inspiration
In the post-Covid era, the abrupt transition to zoom calls and social isolation had great impacts of socializing and communication skills, which still carry on today. 
Often times, we feel nervous before a job, college, or internship interview, and Skib is the perfect tool to ensure your confidence. 
As they say, you are your hardest critic. This is why Skib gives users the opportunity to reflect on their own speaking skills and learn from our data analysis for points of improvement before the big day.

### What is SKIB?
SKIB utilizes computer speech recognition, generative AI, and tone analysis to provide feedback for the user’s speech. We look at both the audio, as well as the transcript along with timestamps to check for the speaker’s use of filler words (like, um, etc.), number of pauses, vocabulary usage, pace of speech, and volume of speech to suggest the user potential points of improvement.
In addition, we do fast foward fourier analysis to determine the fluctuation of the user’s tone, to make sure that the user’s speech is not too monotone

### Tools and Libraries used
Frontend: <pre> HTML, CSS, Tailwind, Matplotlib </pre>
Backend: <pre> Flask, OpenAI API, Librosa, SpeechRecognition </pre>

### Next steps
In the future, we will adapt this technology for different languages. Currently computer speech recognition works with English, Chinese, Hindi, Spanish & French, however; due to the different structures of those languages, they each will need their own set of speech quality analysis rules.
Furthermore, we aim to make SKIB more mobile friendly through an app. 





