const defaultTheme = require("tailwindcss/defaultTheme");

const config = {
	mode: 'jit',
	purge: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		extend: {
			fontFamily: {
        sans: ["Roboto", ...defaultTheme.fontFamily.sans]
      },
			colors: {
        'gray-3': '#333333',
      }
		}
	},

	plugins: []
};

module.exports = config;
