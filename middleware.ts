import { NextRequest, NextResponse } from "next/server";

export function middleware(request: NextRequest) {
  const host = (request.headers.get("host") || request.nextUrl.host).split(":")[0].toLowerCase();
  const path = request.nextUrl.pathname;
  const wikiHost = host === "wiki.ketanshukla.dev";
  const courseHost = host === "course.ketanshukla.dev";
  if (wikiHost && path === "/how-to-use") {
    return NextResponse.redirect(new URL("https://course.ketanshukla.dev/how-to-use"), 307);
  }
  // Canonical wiki addresses never expose the internal /wiki route prefix.
  if ((wikiHost || courseHost) && (path === "/wiki" || path.startsWith("/wiki/"))) {
    const target = new URL(request.nextUrl);
    target.host = "wiki.ketanshukla.dev";
    target.protocol = "https:";
    target.port = "";
    target.pathname = path.slice(5) || "/";
    return NextResponse.redirect(target, 308);
  }
  if (wikiHost) {
    const target = request.nextUrl.clone();
    target.pathname = `/wiki${path === "/" ? "" : path}`;
    return NextResponse.rewrite(target);
  }
  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next/|api/|library/|favicon.ico|robots.txt|sitemap.xml).*)"],
};
