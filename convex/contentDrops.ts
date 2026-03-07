import { query, mutation } from "./_generated/server";
import { v } from "convex/values";

export const list = query({
  args: {},
  handler: async (ctx) => {
    const drops = await ctx.db.query("content_drops").collect();
    return drops.sort((a, b) => b.createdAt - a.createdAt);
  },
});

export const get = query({
  args: { id: v.id("content_drops") },
  handler: async (ctx, args) => {
    return await ctx.db.get(args.id);
  },
});

export const create = mutation({
  args: {
    title: v.string(),
    description: v.string(),
    category: v.union(
      v.literal("marketing"),
      v.literal("code"),
      v.literal("spec"),
      v.literal("email"),
      v.literal("social"),
      v.literal("other")
    ),
    files: v.array(
      v.object({
        name: v.string(),
        content: v.string(),
        mimeType: v.string(),
        size: v.number(),
      })
    ),
    status: v.optional(
      v.union(
        v.literal("pending"),
        v.literal("reviewed"),
        v.literal("used"),
        v.literal("rejected")
      )
    ),
    createdBy: v.string(),
    linkedTask: v.optional(v.id("tasks")),
    notes: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    return await ctx.db.insert("content_drops", {
      ...args,
      status: args.status ?? "pending",
      createdAt: Date.now(),
    });
  },
});

export const updateStatus = mutation({
  args: {
    id: v.id("content_drops"),
    status: v.union(
      v.literal("pending"),
      v.literal("reviewed"),
      v.literal("used"),
      v.literal("rejected")
    ),
  },
  handler: async (ctx, args) => {
    const { id, status } = args;
    const drop = await ctx.db.get(id);
    if (!drop) throw new Error("Content drop not found");

    await ctx.db.patch(id, { status });
  },
});

export const addNotes = mutation({
  args: {
    id: v.id("content_drops"),
    notes: v.string(),
  },
  handler: async (ctx, args) => {
    const { id, notes } = args;
    const drop = await ctx.db.get(id);
    if (!drop) throw new Error("Content drop not found");

    await ctx.db.patch(id, { notes });
  },
});
