import Link from "next/link";
export default function WikiNotFound(){return <main id="wiki-content" className="wiki-main"><h1>That concept is not in the wiki yet.</h1><p>Try the concept index to find a related topic.</p><Link prefetch={false} href="/wiki">Browse the wiki →</Link></main>;}
