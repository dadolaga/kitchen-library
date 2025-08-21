import type { Metadata } from "next";

export const metadata: Metadata = {
    title: "Kithen book",
    description: "This app contain all receipe",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
            <body>
                {children}
            </body>
        </html>
    );
}
