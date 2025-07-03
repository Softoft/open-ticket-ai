import {readonly} from 'vue';
// Make sure the path to your JSON file is correct relative to the .vitepress directory
import apiJsonData from '../api_reference.json';

// --- TYPE DEFINITIONS ---
// These types should match the structure of your generated JSON file.

export interface ParameterData {
    name?: string | null;
    type?: string | null;
    default?: string | null;
    is_optional?: boolean | null;
    description?: string | null;
}

export interface ReturnsData {
    type?: string | null;
    description?: string | null;
    name?: string | null;
}

export interface DocstringData {
    short_description?: string | null;
    long_description?: string | null;
    params: ParameterData[];
    raises: ParameterData[];
    returns?: ReturnsData | null;
}

export interface FunctionData {
    name: string;
    signature: string;
    is_async: boolean;
    docstring: DocstringData;
}

export interface ClassData {
    name: string;
    docstring: DocstringData;
    methods: FunctionData[];
}

// This is the structure of each element in the root JSON array
export interface ModuleEntry {
    module_path: string;
    module_docstring: DocstringData;
    classes: ClassData[];
    functions: FunctionData[];
}

// This will be the type stored in the Map, with module_path added for context
export interface ClassDataWithContext extends ClassData {
    module_path: string;
}

export interface FunctionDataWithContext extends FunctionData {
    module_path: string;
}


// --- DATA STORE ---

// Type the raw JSON data import
const apiData: ModuleEntry[] = apiJsonData;

// This will hold our processed, easily searchable data with strong types
const processedData = {
    packages: new Map<string, ModuleEntry>(),
    classes: new Map<string, ClassDataWithContext>(),
    functions: new Map<string, FunctionDataWithContext>(),
};

/**
 * Processes the raw API data from JSON into structured Maps for efficient lookups.
 * This function runs only once.
 */
function processApiData() {
    // Guard to prevent processing more than once
    if (processedData.packages.size > 0) return;

    for (const module of apiData) {
        const modulePath = module.module_path;

        // 1. Store the entire module data by its path
        processedData.packages.set(modulePath, module);

        // 2. Store each class with a unique, searchable ID (e.g., 'path/to/file.py.ClassName')
        if (module.classes) {
            for (const cls of module.classes) {
                const classId = `${modulePath}.${cls.name}`;
                // Store class data along with its module path for context
                processedData.classes.set(classId, {...cls, module_path: modulePath});
            }
        }

        // 3. Store each top-level function with a unique, searchable ID
        if (module.functions) {
            for (const func of module.functions) {
                const funcId = `${modulePath}.${func.name}`;
                processedData.functions.set(funcId, {...func, module_path: modulePath});
            }
        }
    }
}

// Run the processing logic as soon as this module is imported
processApiData();

/**
 * A Vue composable that provides reactive, read-only access to the processed API documentation.
 */
export function useApiDocs() {
    return {
        packages: readonly(processedData.packages),
        classes: readonly(processedData.classes),
        functions: readonly(processedData.functions),
    };
}

