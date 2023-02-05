import '@/scss/global.scss';
import type { AppProps } from 'next/app';
import Head from 'next/head';
import Header from '@/components/Header/Header';

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>Paczaj WTF</title>
      </Head>
      <div className="app">
        <Header />
        <main className="main__layout">
          <Component {...pageProps} />
        </main>
      </div>
    </>
  );
}
