/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './MyInvest/investApp/templates/**/*.html'
  ],
  theme: {
    extend: {
      animation:{
        marquee:'marquee 10s linear infinite',
        marquee2:'marquee 10s linear infinite',
      },
      keyframes:{
        marquee:{
          '0%' : {transform:'translateX(0%)'},
          '100%' : {transform:'translateX(-100%)'},
        },
        marquee2:{
          '0%' : {transform:'translateX(100%)'},
          '100%' : {transform:'translateX(0%)'},
          
        },
      },

    },
  },
  variants:{},
  plugins: [],



}

