<template>
  <div id="redoc-container"></div>
</template>

<script>
import {onMounted, onUnmounted} from 'vue'

const breakpoints = {
  small: '680px',
  medium: '4000px',
  large: '5000px',
}
const lightTheme = {
  breakpoints,
  typography: {
    fontSize: "1rem",
    fieldName: {
      fontSize: "1rem",
    },
    code: {
      fontSize: "1rem",
    },
  },
}
const darkTheme = {
  breakpoints,
  codeBlock: {
    backgroundColor: '#18181b',
  },
  colors: {
    error: {
      main: '#ef4444',
    },
    border: {
      light: '#27272a',
      dark: '#a1a1aa',
    },
    http: {
      basic: '#71717a',
      delete: '#ef4444',
      get: '#22c55e',
      head: '#d946ef',
      link: '#06b6d4',
      options: '#eab308',
      patch: '#f97316',
      post: '#3b82f6',
      put: '#ec4899',
    },
    primary: {
      main: '#71717a',
    },
    responses: {
      error: {
        backgroundColor: 'rgba(239,68,68,0.1)',
        borderColor: '#fca5a5',
        color: '#ef4444',
        tabTextColor: '#ef4444',
      },
      info: {
        backgroundColor: 'rgba(59,131,246,0.1)',
        borderColor: '#93c5fd',
        color: '#3b82f6',
        tabTextColor: '#3b82f6',
      },
      redirect: {
        backgroundColor: 'rgba(234,179,8,0.1)',
        borderColor: '#fde047',
        color: '#eab308',
        tabTextColor: '#eab308',
      },
      success: {
        backgroundColor: 'rgba(34,197,94,0.1)',
        borderColor: '#86efac',
        color: '#22c55e',
        tabTextColor: '#22c55e',
      },
      warning: {
        main: '#eab308',
      },
    },
    secondary: {
      main: '#3f3f46',
      light: '#27272a',
    },
    success: {
      main: '#22c55e',
    },
    text: {
      primary: '#fafafa',
      secondary: '#d4d4d8',
      light: '#3f3f46',
    },
  },
  fab: {
    backgroundColor: '#52525b',
    color: '#67e8f9',
  },
  rightPanel: {
    backgroundColor: '#27272a',
    servers: {
      overlay: {
        backgroundColor: '#27272a',
      },
      url: {
        backgroundColor: '#18181b',
      },
    },
  },
  schema: {
    linesColor: '#d8b4fe',
    typeNameColor: '#93c5fd',
    typeTitleColor: '#1d4ed8',
  },
  sidebar: {
    activeTextColor: '#ffffff',
    backgroundColor: '#18181b',
    textColor: '#a1a1aa',
  },
  typography: {
    code: {
      backgroundColor: '#18181b',
      color: '#fde047',
      fontSize: "1rem",
    },
    fieldName: {
      fontSize: "1rem",
    },
    links: {
      color: '#0ea5e9',
      hover: '#0ea5e9',
      textDecoration: 'none',
      hoverTextDecoration: 'underline',
      visited: '#0ea5e9',
    },
    fontSize: "1rem",
  },
  extensionsHook: (c) => {
    if (c === 'UnderlinedHeader') {
      return {
        color: '#a1a1aa',
        fontWeight: 'bold',
        borderBottom: '1px solid #3f3f46',
      };
    }
  },
};
export default {
  props: {
    specUrl: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    let redocInitialized = false;
    let observer;
    const initializeRedoc = () => {
      const redocContainer = document.getElementById('redoc-container');
      if (!redocContainer) return;

      if (redocInitialized) {
        redocContainer.innerHTML = '';
      }

      if (document.documentElement.classList.contains('dark')) {
        window.Redoc.init(props.specUrl, {theme: darkTheme}, redocContainer);
      } else {
        window.Redoc.init(props.specUrl, {theme: lightTheme}, redocContainer);
      }
    };

    const observeDarkMode = () => {
      observer = new MutationObserver(() => {
        initializeRedoc();
      });

      observer.observe(document.documentElement, {attributes: true, attributeFilter: ['class']});


    };

    onMounted(() => {
      const script = document.createElement('script');
      script.src = 'https://cdn.jsdelivr.net/npm/redoc/bundles/redoc.standalone.js';
      script.async = true;
      script.onload = () => {
        initializeRedoc();
        observeDarkMode();
      };
      document.head.appendChild(script);
    });
    onUnmounted(() => {
      observer.disconnect();
    });
  },
}
</script>

<style>
/* .vitepress/redoc-dark.css */
.dark #redoc-container {
  background-color: var(--vp-c-bg);
  color: var(--vp-c-text-1);
}

.dark #redoc-container .menu-content {
  background-color: var(--vp-c-bg-alt);
}

.dark #redoc-container .menu-content a {
  color: var(--vp-c-text-1);
}

.dark #redoc-container .menu-content a:hover {
  color: var(--vp-c-brand-1);
}

.dark #redoc-container .swagger-ui .topbar {
  background-color: var(--vp-c-bg-alt);
}

.dark #redoc-container .swagger-ui .topbar .download-url-wrapper {
  color: var(--vp-c-text-1);
}

.dark #redoc-container .redoc-markdown h1,
.dark #redoc-container .redoc-markdown h2,
.dark #redoc-container .redoc-markdown h3,
.dark #redoc-container .redoc-markdown h4,
.dark #redoc-container .redoc-markdown h5,
.dark #redoc-container .redoc-markdown h6 {
  color: var(--vp-c-text-1);
}

.dark #redoc-container .redoc-markdown p {
  color: var(--vp-c-text-2);
}

.dark #redoc-container .redoc-wrap .api-info,
.dark #redoc-container .redoc-wrap .api-info p {
  color: var(--vp-c-text-2);
}

.dark #redoc-container .redoc-wrap .api-info .api-title {
  color: var(--vp-c-text-1);
}

.dark #redoc-container .redoc-wrap .api-info .api-description {
  color: var(--vp-c-text-2);
}

.dark #redoc-container .btn {
  background-color: var(--vp-c-brand-3);
  color: var(--vp-c-neutral-inverse);
}

.dark #redoc-container .btn:hover {
  background-color: var(--vp-c-brand-2);
}

.dark #redoc-container .btn:active {
  background-color: var(--vp-c-brand-1);
}

.dark #redoc-container .swagger-ui .opblock-tag {
  background-color: var(--vp-c-bg-alt);
}

.dark #redoc-container .swagger-ui .opblock .opblock-summary {
  background-color: var(--vp-c-bg-elv);
}

.dark #redoc-container .swagger-ui .opblock .opblock-summary-description {
  color: var(--vp-c-text-2);
}

.dark #redoc-container .swagger-ui .opblock .opblock-summary-method {
  background-color: var(--vp-c-brand-3);
  color: var(--vp-c-neutral-inverse);
}

</style>