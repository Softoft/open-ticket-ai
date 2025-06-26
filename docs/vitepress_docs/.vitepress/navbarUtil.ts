// .vitepress/navbarUtil.ts
import fs from 'fs';
import path from 'path';

// --- TypeScript Interfaces for Clarity ---

// Represents a direct link in the navbar
interface NavbarItem {
    text: string;
    link: string;
}

// Represents a dropdown menu in the navbar
interface NavbarItemGroup {
    text: string;
    items: (NavbarItem | NavbarItemGroup)[]; // An item can be another link or a nested group
}

// A union type for convenience
type NavItem = NavbarItem | NavbarItemGroup;


/**
 * Formats a directory or file name into a human-readable title.
 */
function formatTitle(name: string): string {
    // Removes .md extension and converts 'file-name' to 'File Name'
    const baseName = name.replace(/\.md$/, '');
    return baseName
        .replace(/[-_]/g, ' ')
        .replace(/\b\w/g, (char) => char.toUpperCase());
}

/**
 * Recursively scans a directory to generate nested nav items.
 *
 * @param {string} currentPath - The full filesystem path of the directory to scan.
 * @param {string} docsRootPath - The absolute root path of the 'docs_src' directory.
 * @returns {NavItem[]} - An array of navbar items and groups.
 */
function generateNavItemsRecursive(currentPath: string, docsRootPath: string): NavItem[] {
    try {
        const entries = fs.readdirSync(currentPath, { withFileTypes: true });

        const navItems: NavItem[] = entries
            // Exclude common files/folders you don't want in the nav
            .filter(dirent => !dirent.name.startsWith('.') && dirent.name !== 'index.md')
            .map((dirent): NavItem | null => {
                const fullPath = path.join(currentPath, dirent.name);
                const title = formatTitle(dirent.name);

                if (dirent.isDirectory()) {
                    // --- This is a directory, so create a dropdown group ---
                    return {
                        text: title,
                        // RECURSIVE CALL: Process the subdirectory to get its items
                        items: generateNavItemsRecursive(fullPath, docsRootPath),
                    };
                } else if (dirent.isFile() && dirent.name.endsWith('.md')) {
                    // --- This is a Markdown file, so create a direct link ---

                    // Get the path relative to 'docs_src' (e.g., 'v0_1/en/guide/installation.md')
                    const relativePath = path.relative(docsRootPath, fullPath);

                    // Convert to a web-friendly URL path
                    const link = `/${relativePath.replace(/\\/g, '/')}`;

                    return {
                        text: title,
                        link: link,
                    };
                }
                // Ignore other file types
                return null;
            })
            .filter((item): item is NavItem => item !== null); // Filter out any null values

        return navItems;

    } catch (error) {
        console.error(`❌ Error during recursive scan of ${currentPath}:`, (error as Error).message);
        return [];
    }
}


/**
 * The main function to generate the entire navbar for a specific version and language.
 *
 * @param {string} basePath - The base path for navigation (e.g., 'v0_1/en').
 * @returns {NavItem[]} An array of NavItem objects for the VitePress config.
 */
export function generateNavbar(basePath: string): NavItem[] {
    const docsRootPath = path.resolve(process.cwd(), 'docs_src');
    const directoryToScan = path.join(docsRootPath, basePath);

    console.log(`\n🔍 Recursively scanning navbar items in: ${directoryToScan}`);

    const items = generateNavItemsRecursive(directoryToScan, docsRootPath);

    console.log(`✅ Successfully generated nested navbar with ${items.length} top-level items.`);
    return items;
}
