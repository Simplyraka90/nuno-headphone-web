// @ts-ignore CSS is loaded by Next.js at runtime; it has no TypeScript exports.
import './globals.css';
import type { Metadata } from 'next';
import { Shell } from '@/components/Shell';

export const metadata: Metadata = {
	title: 'NUNO — Sound in its purest form',
	description: 'Explore the NUNO headphone concept in interactive 3D.',
};

export default function Layout({ children }: { children: React.ReactNode }) {
	return (
		<html lang="en">
			<body>
				<Shell>{children}</Shell>
			</body>
		</html>
	);
}
