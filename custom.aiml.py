<aiml version="1.0.1" encoding="UTF-8">

   <category>

       <pattern>I * To *</pattern>

       <template>I do not <star index = "1"/> to <star index = "2"/>?</template>

   </category>

   <category>

	<pattern>I * to *</pattern>

	<template>I do not <star index = "1"/> to <star index = "2"/></template>

   </category>

   
   <category>

	<pattern>I * at *</pattern>

	<template>Do i <star index = "1"/> at <star index = "2"/>?</template>

   </category>

   <category>

	<pattern>I am * at *</pattern>

	<template>I am not <star index = "1"/> at <star index = "2"/></template>

   </category>


   <category>

	<pattern>I am * in *</pattern>

	<template>Am i <star index = "1"/> in <star index = "2"/>?</template>

   </category>

</aiml>