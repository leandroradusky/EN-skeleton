import * as path from 'path'

import adapter from '@sveltejs/adapter-static'
import sveltePreprocess from 'svelte-preprocess'
import autoprefixer from 'autoprefixer'

const dev = process.env.NODE_ENV === 'development'

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    // hydrate the <div id="svelte"> element in src/app.html
    target: '#svelte',
    adapter: adapter({
      // default options are shown
      pages: 'build',
      assets: 'build',
      fallback: null,
    }),
    paths: {
      base: dev ? '' : '/static',
    },
    vite: {
      resolve: {
        alias: {
          $store: path.resolve('./src/store'),
        },
      },
      plugins: [autoprefixer],
    },
  },

  preprocess: [
    sveltePreprocess({
      sourceMap: dev,
      scss: {
        prependData: `@import 'src/styles/variables.scss';`,
      },
    }),
  ],
}

export default config
