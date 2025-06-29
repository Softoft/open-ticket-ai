// .vitepress/navbarUtil.ts
import fs from 'fs';
import path from 'path';

interface NavbarItem {
    text: string;
    link: string;
}

interface NavbarItemGroup {
    text: string;
    items: (NavbarItem | NavbarItemGroup)[];
}

type NavItem = NavbarItem | NavbarItemGroup;

function formatTitle(name: string): string {
    const baseName = name.replace(/\.md$/, '');
    return baseName.replace(/[-_]/g, ' ').replace(/\b\w/g, (char) => char.toUpperCase());
}

function generateNavItemsRecursive(currentPath: string, docsRootPath: string): NavItem[] {
    try {
        const entries = fs.readdirSync(currentPath, {withFileTypes: true});
        return entries
            .filter(dirent => {
                !dirent.name.startsWith('.')
                && !dirent.name.startsWith('_')
                && dirent.name !== 'index.md'
            })
            .map((dirent): NavItem | null => {
                const fullPath = path.join(currentPath, dirent.name);
                const title = formatTitle(dirent.name);
                if (dirent.isDirectory()) {
                    return {
                        text: title,
                        items: generateNavItemsRecursive(fullPath, docsRootPath),
                    };
                } else if (dirent.isFile() && dirent.name.endsWith('.md')) {
                    const relativePath = path.relative(docsRootPath, fullPath);
                    const link = `${relativePath.replace(/\\/g, '/')}`;
                    return {text: title, link};
                }
                return null;
            })
            .filter((item): item is NavItem => item !== null);
    } catch (error) {
        console.error(`❌ Error scanning ${currentPath}:`, (error as Error).message);
        return [];
    }
}

/**
 * The main function to generate the navbar.
 * THIS FUNCTION IS NOW FIXED.
 * @param {string} basePath - The base path for navigation (e.g., 'en/v0_1').
 */
export function generateNavbar(basePath: string): NavItem[] {
    const docsRootPath = path.resolve(process.cwd(), 'docs_src');

    const directoryToScan = path.join(docsRootPath, basePath);

    console.log(`\n🔍 Recursively scanning navbar items in: ${directoryToScan}`);

    const items = generateNavItemsRecursive(directoryToScan, docsRootPath);

    console.log(`✅ Generated nested navbar with ${items.length} top-level items.`);
    console.log(JSON.stringify(items))
    return items;
}
