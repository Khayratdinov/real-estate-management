import LeftNavbar from "@/components/shared/navbar/LeftNavbar";
import Navbar from "@/components/shared/navbar/Navbar";
import React from "react";

interface LayoutProps {
	children: React.ReactNode;
}

export default function layout({ children }: LayoutProps) {
	return (
		<main className="bg-baby_veryBlack relative">
			<Navbar />
			<div className="flex">
				{/* placeholder LeftNavbar component */}
				<LeftNavbar />
				<section className="flex min-h-screen flex-1 flex-col px-4 pb-6 pt-24 sm:px-6 lg:px-8 lg:pt-32">
					<div>{children}</div>
				</section>
				{/* placeholder right navbar component */}
				<div className="dark:text-pumpkin hidden text-xl md:block">
					Right Navbar
				</div>
			</div>
		</main>
	);
}

// npm i react-hook-form@7.50.1 @hookform/resolvers@3.3.4 zod@3.22.4 react-toastify@10.0.4 react-redux@9.1.0 @reduxjs