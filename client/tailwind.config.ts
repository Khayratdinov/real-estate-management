import type { Config } from "tailwindcss";

const config: Config = {
    darkMode: ["class"],
    content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
  	extend: {
  		backgroundImage: {
  			'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
  			'gradient-conic': 'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))'
  		},
  		borderRadius: {},
  		colors: {
			googleBlue: "#4285F4",
			asparagus: "#60992D",
			deepBlueGrey: "#263238",
			gray: "rgba(125,144,201,0.34)",
			lightGray: "#7B8EC8",
			electricIndigo: "#6610F2",
			richBlack: "#0D1317",
			veryBlack: "#000000",
			babyPowder: "#FBFEF9",
			pumpkin: "#F17105",
			platinum: "#DDE1E4",
			lightGrey: "#EEEEEE",
			pear: "#C2E812",
			eerieBlack: "#171D1C",
			ballonWhite: "#dfe6f6",
		},
		fontFamily: {
			openSans: ["var(--font-openSans)"],
			robotoSlab: ["var(--font-robotoSlab)"],
		},
		
  	}
  },
  plugins: [require("tailwindcss-animate")],
};
export default config;
