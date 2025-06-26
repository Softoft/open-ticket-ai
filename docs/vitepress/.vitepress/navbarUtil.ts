import fs from 'fs';
import path from 'path';

/**
 * Represents the structure of a single item in the VitePress navigation bar.
 */
interface NavItem {
    text: string;
    link: string;
    activeMatch?: string;
}

/**
 * Formats a directory or file name into a human-readable title.
 * - Replaces hyphens with spaces.
 * - Capitalizes the first letter of each word.
 * @param name The raw directory or file name.
 * @returns A formatted string suitable for display text.
 */
function formatTitle(name: string): string {
    // Remove file extensions like .md if they exist
    const baseName = name.replace(/\.md$/, '');
    // Replace hyphens/underscores with spaces and capitalize words
    return baseName
        .replace(/[-_]/g, ' ')
        .replace(/\b\w/g, (char) => char.toUpperCase());
}

/**
 * Generates a VitePress navbar configuration by scanning a directory's subdirectories.
 * It creates a nav item for each immediate subdirectory found.
 *
 * @param docsRoot - The root directory of your documentation files (e.g., 'src' or 'docs').
 * @returns An array of NavItem objects for the VitePress themeConfig.
 */
export function generateNavbar(docsRoot: string): NavItem[] {
    // Resolve the absolute path to the documentation root directory
    const rootPath = path.resolve(process.cwd(), docsRoot);

    console.log(`Scanning for navbar items in: ${rootPath}`);

    try {
        // Read all entries (files and directories) from the root path
        const entries = fs.readdirSync(rootPath, {withFileTypes: true});

        const navItems: NavItem[] = entries
            // Filter out files, leaving only directories
            .filter(dirent => dirent.isDirectory())
            // Filter out special VitePress directories or hidden folders
            .filter(dirent => dirent.name !== '.vitepress' && !dirent.name.startsWith('_'))
            // Map the remaining directory names to NavItem objects
            .map(dirent => {
                const directoryName = dirent.name;
                // The link should be an absolute path from the project root
                const link = `/${directoryName}/`;

                console.log(`- Found directory: ${directoryName}, creating link: ${link}`);

                return {
                    text: formatTitle(directoryName),
                    link: link,
                    // activeMatch helps VitePress highlight the correct nav item.
                    // This rule highlights the nav item if the URL starts with its link.
                    activeMatch: `^${link}`,
                };
            });

        console.log('Successfully generated navbar items:', navItems);
        return navItems;
    } catch (error) {
        console.error(`Error scanning directory ${rootPath}:`, error);
        // Return an empty array or handle the error as needed
        return [];
    }
}
