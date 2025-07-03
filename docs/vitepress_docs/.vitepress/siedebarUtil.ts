// .vitepress/sidebarUtil.ts (or wherever you prefer)
import fs from 'fs';
import path from 'path';

// You can reuse these types from your navbar util
interface SidebarItem {
    text: string;
    link: string;
}

interface SidebarItemGroup {
    text: string;
    items: (SidebarItem | SidebarItemGroup)[];
    collapsible?: boolean;
    collapsed?: boolean;
}

type SidebarNavItem = SidebarItem | SidebarItemGroup;

function formatTitle(name: string): string {
    const baseName = name.replace(/\.md$/, '');
    return baseName.replace(/[-_]/g, ' ').replace(/\b\w/g, (char) => char.toUpperCase());
}

/**
 * Generates the items for a single sidebar section (e.g., for 'api' or 'guide').
 * This is a slightly modified version of your recursive function.
 */
function generateSidebarItems(dirPath: string, rootPath: string): SidebarNavItem[] {
    const entries = fs.readdirSync(dirPath, {withFileTypes: true});
    return entries
        .filter(dirent => !dirent.name.startsWith('.') && dirent.name !== 'index.md')
        .map((dirent): SidebarNavItem => {
            const fullPath = path.join(dirPath, dirent.name);
            const relativePath = `/${path.relative(rootPath, fullPath).replace(/\\/g, '/')}`;

            if (dirent.isDirectory()) {
                return {
                    text: formatTitle(dirent.name),
                    items: generateSidebarItems(fullPath, rootPath),
                    collapsible: true, // Good practice for nested items
                    collapsed: true,   // Start collapsed to keep it clean
                };
            } else {
                return {
                    text: formatTitle(dirent.name),
                    link: relativePath,
                };
            }
        });
}

/**
 * The main function to generate the entire multi-sidebar configuration.
 * Call this from your config file.
 * @param {string} basePath - The base content directory (e.g., 'en').
 */
export function generateMultiSidebar(basePath: string) {
    const rootPath = path.resolve(process.cwd(), 'docs_src'); // Adjust if docs_src is not at root
    const contentPath = path.join(rootPath, basePath);

    const sidebar: Record<string, SidebarNavItem[]> = {};

    const topLevelDirs = fs.readdirSync(contentPath, {withFileTypes: true})
        .filter(dirent => dirent.isDirectory() && !dirent.name.startsWith('.'));

    for (const dir of topLevelDirs) {
        const sectionPath = `/${basePath}/${dir.name}/`;
        const sectionFullPath = path.join(contentPath, dir.name);

        // The key for the sidebar object, e.g., '/en/api/'
        sidebar[sectionPath] = [{
            text: formatTitle(dir.name),
            items: generateSidebarItems(sectionFullPath, rootPath)
        }];
    }

    return sidebar;
}
