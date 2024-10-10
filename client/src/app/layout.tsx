import { ThemeProvider } from "@/components/theme-provider";
import { openSans, robotoSlab } from "@/lib/fonts";
import type { Metadata } from "next";
import React from "react";
import "./globals.css";

import Toast from "@/components/shared/Toast";
import ReduxProvider from "@/lib/redux/provider";

export const metadata: Metadata = {
	title: "Home | NP Apartments",
	description: "Welcome home",
};

export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) {
	return (
		<html lang="en" suppressHydrationWarning>
			<body className={`${openSans.variable} ${robotoSlab.variable}`}>
				<Toast />
				<ReduxProvider>
					<ThemeProvider
						attribute="class"
						defaultTheme="system"
						enableSystem
						disableTransitionOnChange
					>
						{children}
					</ThemeProvider>
				</ReduxProvider>
			</body>
		</html>
	);
}