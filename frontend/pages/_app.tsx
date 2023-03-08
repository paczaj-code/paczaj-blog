import '@/scss/global.scss';
import type { AppProps } from 'next/app';
import Head from 'next/head';
import Header from '@/components/Header/Header';
import 'prismjs/themes/prism-tomorrow.css';
import Layout from 'layouts/Layout';
export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>Paczaj WTF</title>
      </Head>
      <div className="app">
        <Header />
        <Component {...pageProps} />
      </div>
    </>
  );
}
